"""
Views for graph presets and organizational unit filtering.
"""
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from ontology.models import OModel
from ontology.services.graph_presets import GraphPresetService
from openea.constants import Utils
from utils.views.custom import SingleObjectView


class OModelPresetsView(LoginRequiredMixin, SingleObjectView, View):
    """
    API endpoint for getting graph presets for a model.
    GET /o_model/<model_id>/presets/
    """
    model = OModel
    permission_required = [(Utils.PERMISSION_ACTION_VIEW, model.get_object_type(), None)]

    def get(self, request, *args, **kwargs):
        model_id = kwargs.pop('model_id')
        model = OModel.objects.get(id=model_id)

        presets = GraphPresetService.get_presets(model.organisation)

        return JsonResponse(presets, safe=False)


class OModelPresetsUpdateView(LoginRequiredMixin, SingleObjectView, View):
    """
    API endpoint for updating graph presets for a model's organisation.
    POST /o_model/<model_id>/presets/
    """
    model = OModel
    permission_required = [(Utils.PERMISSION_ACTION_UPDATE, model.get_object_type(), None)]

    def post(self, request, *args, **kwargs):
        model_id = kwargs.pop('model_id')
        model = OModel.objects.get(id=model_id)

        data = json.loads(request.body)
        presets = data.get('presets', {})

        GraphPresetService.save_presets(model.organisation, presets)

        return JsonResponse({'status': 'success'})


class OModelOrgUnitsView(LoginRequiredMixin, SingleObjectView, View):
    """
    API endpoint for getting organizational units available in a model.
    GET /o_model/<model_id>/org_units/
    """
    model = OModel
    permission_required = [(Utils.PERMISSION_ACTION_VIEW, model.get_object_type(), None)]

    def get(self, request, *args, **kwargs):
        model_id = kwargs.pop('model_id')
        model = OModel.objects.get(id=model_id)

        org_units = GraphPresetService.get_org_units(model)

        return JsonResponse({'org_units': org_units}, safe=False)


class OModelOrgUnitInstancesView(LoginRequiredMixin, SingleObjectView, View):
    """
    API endpoint for getting instances owned by an organizational unit.
    GET /o_model/<model_id>/org_units/<org_unit_id>/instances/
    """
    model = OModel
    permission_required = [(Utils.PERMISSION_ACTION_VIEW, model.get_object_type(), None)]

    def get(self, request, *args, **kwargs):
        model_id = kwargs.pop('model_id')
        org_unit_id = kwargs.pop('org_unit_id')
        model = OModel.objects.get(id=model_id)

        include_children = request.GET.get('include_children', 'true').lower() == 'true'

        instance_ids = GraphPresetService.get_instances_by_org_unit(
            model, org_unit_id, include_children=include_children
        )

        return JsonResponse({'instance_ids': instance_ids}, safe=False)
