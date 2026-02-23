import json
from uuid import UUID

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from django.views.generic import View
from ontology.controllers.o_model import ModelUtils

from ontology.models import OConcept, OInstance, OModel, OPredicate, ORelation
from ontology.plugins.json import GenericEncoder
from openea.constants import Utils


class OModelPathFinderView(LoginRequiredMixin, View):
    permission_required = [(Utils.PERMISSION_ACTION_VIEW, OModel.get_object_type(), None)]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        start_instance_id = ModelUtils.version_uuid(data.get('start_instance_id'))
        start_instance = OInstance.objects.get(id=start_instance_id)

        find_all_of_concept = data.get('find_all_of_concept', False)

        # Extract relation_ids (optional filter)
        relation_ids_raw = data.get('relation_ids', None)
        relation_ids = None
        if relation_ids_raw:
            # Convert to UUID objects and filter out invalid values
            valid_ids = []
            for rid in relation_ids_raw:
                if rid:
                    try:
                        valid_ids.append(UUID(rid))
                    except (ValueError, TypeError):
                        pass
            relation_ids = set(valid_ids) if valid_ids else None

        # Check permissions for start instance
        show_relations = self.request.user.acl.check(organisation=start_instance.organisation, permissions_required=(Utils.PERMISSION_ACTION_VIEW, ORelation.get_object_type(), None))
        show_concepts = self.request.user.acl.check(organisation=start_instance.organisation, permissions_required=(Utils.PERMISSION_ACTION_VIEW, OConcept.get_object_type(), None))
        show_predicates = self.request.user.acl.check(organisation=start_instance.organisation, permissions_required=(Utils.PERMISSION_ACTION_VIEW, OPredicate.get_object_type(), None))
        show_instances = self.request.user.acl.check(organisation=start_instance.organisation, permissions_required=(Utils.PERMISSION_ACTION_VIEW, OInstance.get_object_type(), None))

        if not (show_relations and show_concepts and show_predicates and show_instances):
            raise PermissionDenied('Permission Denied')

        if find_all_of_concept:
            # Multi-target mode: find paths to all instances of a concept
            end_concept_id = ModelUtils.version_uuid(data.get('end_concept_id'))
            end_concept = OConcept.objects.get(id=end_concept_id)

            if start_instance.organisation != end_concept.organisation:
                raise PermissionDenied('Organisation mismatch')

            max_results = int(data.get('max_results', 50))
            result = ModelUtils.find_paths_to_concept(
                start_instance=start_instance,
                end_concept=end_concept,
                max_results=max_results,
                relation_ids=relation_ids
            )
        else:
            # Single-instance mode: find path between two specific instances
            end_instance_id = ModelUtils.version_uuid(data.get('end_instance_id'))
            end_instance = OInstance.objects.get(id=end_instance_id)

            if start_instance.organisation != end_instance.organisation:
                raise PermissionDenied('Organisation mismatch')

            result = ModelUtils.find_paths(
                start_instance=start_instance,
                end_instance=end_instance,
                relation_ids=relation_ids
            )

        return HttpResponse(json.dumps(result, cls=GenericEncoder), content_type="application/json")
