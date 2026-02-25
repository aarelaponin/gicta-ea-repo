import json
import logging

from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from ontology.controllers.graphviz import GraphvizController
from ontology.controllers.o_model import ModelUtils
from ontology.models import OModel
from ontology.services.graph_presets import GraphPresetService
from openea.constants import Utils
from utils.views.custom import SingleObjectView

logger = logging.getLogger(__name__)


class OModelGraphView(LoginRequiredMixin, SingleObjectView, View):
    model = OModel
    permission_required = [(Utils.PERMISSION_ACTION_VIEW, model.get_object_type(), None)]

    def post(self, request, *args, **kwargs):
        model_id = kwargs.pop('model_id')
        model = OModel.objects.get(id=model_id)

        data = json.loads(request.body)
        knowledge_set = data.get('knowledge_set', 'instances')

        # Debug logging
        logger.info(f"=== GRAPH VIEW REQUEST ===")
        logger.info(f"display_mode in request: {data.get('display_mode')}")
        selected_ids = data.get('selected_concept_ids', [])
        logger.info(f"selected_concept_ids in request: {len(selected_ids)} items: {selected_ids[:5]}...")

        # Handle org unit filtering
        org_unit_id = data.get('org_unit_id')
        display_mode = data.get('display_mode', 'context')
        selected_concept_ids = data.get('selected_concept_ids', [])

        if org_unit_id:
            # Get instances owned by the org unit
            include_subordinates = data.get('include_subordinates', True)
            logger.info(f"Org unit filtering: org_unit_id={org_unit_id}, include_subordinates={include_subordinates}")

            owned_instance_ids = GraphPresetService.get_instances_by_org_unit(
                model, org_unit_id, include_children=include_subordinates
            )
            logger.info(f"Found {len(owned_instance_ids)} instances owned by org unit")

            # Check if we need transitive filtering (strict mode + non-Application layer)
            # This handles the case where user selects org unit + Data layer + Strict mode
            # We need to find DataEntities connected to Applications owned by org unit
            if display_mode == 'strict' and selected_concept_ids:
                app_concept_ids = set(GraphPresetService.get_application_concept_ids(model))
                selected_set = set(selected_concept_ids)

                # If selected concepts don't include Applications, use transitive filtering
                if not (selected_set & app_concept_ids):
                    logger.info("Transitive filtering: selected concepts don't include Applications")
                    logger.info(f"Finding items connected to {len(owned_instance_ids)} owned instances")

                    # Find items connected to owned instances, filtered by selected concepts
                    connected_ids = GraphPresetService.get_connected_instances(
                        model, owned_instance_ids, target_concept_ids=list(selected_set)
                    )

                    logger.info(f"Found {len(connected_ids)} connected instances of selected concepts")

                    # Use connected instances - if none found, graph will be empty (correct behavior)
                    # Don't fall back to owned_instance_ids as they would be filtered out by strict mode
                    data['instance_ids'] = connected_ids if connected_ids else []

                    # Mark that we've done transitive filtering with concept constraints
                    data['_transitive_filtered'] = True
                else:
                    # Selected concepts include Applications, use direct ownership filtering
                    existing_instance_ids = data.get('instance_ids', [])
                    if existing_instance_ids:
                        filtered_ids = [iid for iid in existing_instance_ids if iid in owned_instance_ids]
                        logger.info(f"Filtered from {len(existing_instance_ids)} to {len(filtered_ids)} instances")
                        data['instance_ids'] = filtered_ids if filtered_ids else owned_instance_ids
                    else:
                        data['instance_ids'] = owned_instance_ids
            else:
                # Context mode or no concept filter - use direct ownership filtering
                existing_instance_ids = data.get('instance_ids', [])
                if existing_instance_ids:
                    filtered_ids = [iid for iid in existing_instance_ids if iid in owned_instance_ids]
                    logger.info(f"Filtered from {len(existing_instance_ids)} to {len(filtered_ids)} instances")
                    data['instance_ids'] = filtered_ids if filtered_ids else owned_instance_ids
                else:
                    data['instance_ids'] = owned_instance_ids

        # Save transitive filter flag before ModelUtils.filter() (which returns new dict)
        transitive_filtered = data.get('_transitive_filtered', False)

        # Apply ModelUtils filter (returns new dict)
        data = ModelUtils.filter(user=self.request.user, data=data)
        data['model'] = model
        data['_transitive_filtered'] = transitive_filtered

        logger.info(f"Display mode: {display_mode}, selected concepts: {len(selected_concept_ids)}, transitive_filtered: {transitive_filtered}")

        # Get slots count before filtering
        slots_before = len(data.get('slots', []))
        logger.info(f"Slots before strict filter: {slots_before}")

        if display_mode == 'strict' and selected_concept_ids and not transitive_filtered:
            # Filter slots to only include those where BOTH subject and object
            # are instances of selected concepts
            selected_concept_ids_set = set(selected_concept_ids)
            logger.info(f"Strict mode: filtering by {len(selected_concept_ids_set)} concept IDs")

            slots = data.get('slots', [])
            filtered_slots = []
            for slot in slots:
                subject_concept_id = str(slot.subject.concept.id) if slot.subject else None
                object_concept_id = str(slot.object.concept.id) if slot.object else None

                subject_ok = subject_concept_id in selected_concept_ids_set
                object_ok = object_concept_id in selected_concept_ids_set

                if subject_ok and object_ok:
                    filtered_slots.append(slot)

            logger.info(f"Strict mode: filtered from {len(slots)} to {len(filtered_slots)} slots")
            data['slots'] = filtered_slots

            # Also filter instances to only include those of selected concepts
            instances = data.get('instances', [])
            filtered_instances = [
                inst for inst in instances
                if str(inst.concept.id) in selected_concept_ids_set
            ]
            logger.info(f"Strict mode: filtered instances from {len(instances)} to {len(filtered_instances)}")
            data['instances'] = filtered_instances
        elif transitive_filtered:
            logger.info(f"Transitive filtering already applied, skipping strict filter. Slots: {slots_before}")
        else:
            logger.info(f"Context mode: keeping all {slots_before} slots")

        svg_str = GraphvizController.render_model_graph(format='svg', model_data=data, knowledge_set=knowledge_set)

        xmlSoup = BeautifulSoup(svg_str, 'html.parser')
        image = xmlSoup.find('svg')
        return HttpResponse(str(image), content_type="text/html")
