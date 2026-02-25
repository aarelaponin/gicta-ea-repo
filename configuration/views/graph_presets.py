"""
Views for managing graph presets configuration.
"""
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from configuration.models import Configuration
from ontology.models import OModel, OConcept, ORelation
from ontology.services.graph_presets import GraphPresetService, DEFAULT_PRESETS
from openea.constants import Utils


class GraphPresetsListView(LoginRequiredMixin, View):
    """
    View for listing and managing graph presets for an organisation.
    GET /configuration/graph_presets/<organisation_id>/
    """

    def get(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')

        # Get current presets
        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)
        presets = GraphPresetService.get_presets(organisation)

        # Get available models for this organisation
        models = OModel.objects.filter(organisation=organisation).order_by('name')

        context = {
            'organisation': organisation,
            'presets': presets,
            'presets_json': json.dumps(presets, indent=2),
            'models': models,
            'default_presets': DEFAULT_PRESETS,
        }

        return render(request, 'configuration/graph_presets/graph_presets_list.html', context)


class GraphPresetsUpdateView(LoginRequiredMixin, View):
    """
    View for updating graph presets.
    POST /configuration/graph_presets/<organisation_id>/update/
    """

    def post(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')

        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)

        # Parse the presets JSON from the form
        presets_json = request.POST.get('presets_json', '{}')
        try:
            presets = json.loads(presets_json)
            GraphPresetService.save_presets(organisation, presets)
        except json.JSONDecodeError:
            # Handle invalid JSON
            pass

        return redirect('graph_presets_list', organisation_id=organisation_id)


class GraphPresetsResetView(LoginRequiredMixin, View):
    """
    View for resetting graph presets to defaults.
    POST /configuration/graph_presets/<organisation_id>/reset/
    """

    def post(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')

        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)

        GraphPresetService.reset_to_defaults(organisation)

        return redirect('graph_presets_list', organisation_id=organisation_id)


class GraphPresetsRoleUpdateView(LoginRequiredMixin, View):
    """
    API view for updating a single role preset.
    POST /configuration/graph_presets/<organisation_id>/role/<role_id>/
    """

    def post(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')
        role_id = kwargs.get('role_id')

        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)

        data = json.loads(request.body)
        role_config = {
            'display_name': data.get('display_name', role_id.replace('_', ' ').title()),
            'description': data.get('description', ''),
            'default_concepts': data.get('default_concepts', []),
            'default_relations': data.get('default_relations', [])
        }

        presets = GraphPresetService.add_role(organisation, role_id, role_config)

        return JsonResponse({'status': 'success', 'presets': presets})

    def delete(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')
        role_id = kwargs.get('role_id')

        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)

        presets = GraphPresetService.remove_role(organisation, role_id)

        return JsonResponse({'status': 'success', 'presets': presets})


class GraphPresetsLayerUpdateView(LoginRequiredMixin, View):
    """
    API view for updating a single layer preset.
    POST /configuration/graph_presets/<organisation_id>/layer/<layer_id>/
    """

    def post(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')
        layer_id = kwargs.get('layer_id')

        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)

        data = json.loads(request.body)
        layer_config = {
            'display_name': data.get('display_name', layer_id.replace('_', ' ').title() + ' Layer'),
            'concepts': data.get('concepts', [])
        }

        presets = GraphPresetService.add_layer(organisation, layer_id, layer_config)

        return JsonResponse({'status': 'success', 'presets': presets})


class GraphPresetsAutoMapView(LoginRequiredMixin, View):
    """
    View for automatically mapping concepts from a model to layers.
    POST /configuration/graph_presets/<organisation_id>/auto_map/<model_id>/
    """

    def post(self, request, *args, **kwargs):
        organisation_id = kwargs.get('organisation_id')
        model_id = kwargs.get('model_id')

        from organisation.models import Organisation
        organisation = Organisation.objects.get(id=organisation_id)
        model = OModel.objects.get(id=model_id)

        # Get all concepts from the model
        concepts = OConcept.objects.filter(model=model, native=False).order_by('name')

        # Auto-map concepts to layers based on name patterns
        layer_mappings = {
            'business': ['business', 'capability', 'service', 'process', 'function', 'value stream'],
            'application': ['application', 'app', 'interface', 'component', 'system'],
            'data': ['data', 'database', 'entity', 'object', 'store'],
            'technology': ['technology', 'infrastructure', 'platform', 'server', 'network', 'hardware']
        }

        presets = GraphPresetService.get_presets(organisation)

        for concept in concepts:
            concept_name_lower = concept.name.lower()
            for layer_id, keywords in layer_mappings.items():
                for keyword in keywords:
                    if keyword in concept_name_lower:
                        GraphPresetService.map_concept_to_layer(organisation, concept.name, layer_id)
                        break

        presets = GraphPresetService.get_presets(organisation)

        return JsonResponse({'status': 'success', 'presets': presets})
