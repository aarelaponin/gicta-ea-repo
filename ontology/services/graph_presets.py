"""
Graph Preset Service for managing architect role presets and layer configurations.

This service provides preset configurations for different EA architect roles
(Business, Application, Data, Technology) and BDAT layer filtering.
"""
import json
from typing import Optional

from configuration.models import Configuration
from ontology.models import OModel, OConcept, ORelation, OInstance, OSlot


# Configuration key for graph presets
GRAPH_PRESETS_CONFIG_NAME = 'graph_presets'

# Default presets for BDAT architect roles
DEFAULT_PRESETS = {
    "roles": {
        "enterprise_architect": {
            "display_name": "Enterprise Architect",
            "description": "Full view across all architecture layers",
            "default_layers": ["business", "application", "data", "technology"],
            "default_concepts": [],  # Will use all concepts from all layers
            "default_relations": []  # Will use all relations
        },
        "business_architect": {
            "display_name": "Business Architect",
            "description": "Focus on business processes, capabilities, and services",
            "default_layers": ["business"],
            "default_concepts": [
                "Business Process",
                "Capability",
                "Service",
                "Business Function",
                "Value Stream",
                "Business Service",
                "Organisation Unit",
                "Strategy"
            ],
            "default_relations": [
                "realizes",
                "supports",
                "enables",
                "owns",
                "performs"
            ]
        },
        "application_architect": {
            "display_name": "Application Architect",
            "description": "Focus on applications, interfaces, and integrations",
            "default_layers": ["application"],
            "default_concepts": [
                "Application",
                "Interface",
                "Application Component",
                "Application Service",
                "Application Function",
                "ApplicationComponent",
                "ApplicationService",
                "ApplicationFunction"
            ],
            "default_relations": [
                "dependsOn",
                "depends-on",
                "uses",
                "realizes",
                "contains",
                "supports",
                "manages",
                "replaces"
            ]
        },
        "data_architect": {
            "display_name": "Data Architect",
            "description": "Focus on data entities, databases, and data flows",
            "default_layers": ["data"],
            "default_concepts": [
                "Data Entity",
                "Data Object",
                "Database",
                "Data Service",
                "Data Store",
                "DataEntity",
                "DataObject"
            ],
            "default_relations": [
                "stores",
                "manages",
                "accesses",
                "transforms",
                "contains",
                "uses"
            ]
        },
        "technology_architect": {
            "display_name": "Technology Architect",
            "description": "Focus on infrastructure, platforms, and technology components",
            "default_layers": ["technology"],
            "default_concepts": [
                "Technology",
                "Infrastructure",
                "Platform",
                "Server",
                "Network",
                "Technology Component",
                "Technology Service",
                "TechnologyComponent",
                "TechnologyService"
            ],
            "default_relations": [
                "hosts",
                "runs-on",
                "deployed-on",
                "supports",
                "provides"
            ]
        }
    },
    "layers": {
        "business": {
            "display_name": "Business Layer",
            "concepts": [
                "Business Process",
                "Capability",
                "Service",
                "Business Function",
                "Organisation Unit",
                "Business Service",
                "Value Stream",
                "Strategy",
                "BusinessProcess",
                "BusinessService",
                "BusinessFunction"
            ]
        },
        "application": {
            "display_name": "Application Layer",
            "concepts": [
                "Application",
                "Interface",
                "Application Component",
                "Application Service",
                "Application Function",
                "ApplicationComponent",
                "ApplicationService",
                "ApplicationFunction"
            ]
        },
        "data": {
            "display_name": "Data Layer",
            "concepts": [
                "Data Entity",
                "Data Object",
                "Database",
                "Data Service",
                "Data Store",
                "DataEntity",
                "DataObject",
                "DataService"
            ]
        },
        "technology": {
            "display_name": "Technology Layer",
            "concepts": [
                "Technology",
                "Infrastructure",
                "Platform",
                "Server",
                "Network",
                "Technology Component",
                "TechnologyComponent",
                "TechnologyService"
            ]
        }
    },
    "org_unit_config": {
        "concept_name": "Organisation Unit",
        "ownership_relation": "ownedBy"
    }
}


class GraphPresetService:
    """Service for managing graph visualization presets."""

    @staticmethod
    def get_presets(organisation) -> dict:
        """
        Get graph presets for an organisation.
        Returns organisation-specific presets if available, otherwise returns defaults.

        Args:
            organisation: The organisation to get presets for

        Returns:
            dict: The presets configuration
        """
        try:
            config = Configuration.objects.get(
                organisation=organisation,
                name=GRAPH_PRESETS_CONFIG_NAME
            )
            if config.content:
                return config.content
        except Configuration.DoesNotExist:
            pass

        return DEFAULT_PRESETS

    @staticmethod
    def save_presets(organisation, presets: dict) -> Configuration:
        """
        Save graph presets for an organisation.

        Args:
            organisation: The organisation to save presets for
            presets: The presets configuration to save

        Returns:
            Configuration: The saved configuration object
        """
        config = Configuration.get_or_create(
            organisation=organisation,
            name=GRAPH_PRESETS_CONFIG_NAME,
            content=presets
        )
        config.content = presets
        config.save()
        return config

    @staticmethod
    def get_role_preset(organisation, role_id: str) -> Optional[dict]:
        """
        Get a specific role preset.

        Args:
            organisation: The organisation
            role_id: The role identifier (e.g., 'business_architect')

        Returns:
            dict or None: The role preset if found
        """
        presets = GraphPresetService.get_presets(organisation)
        roles = presets.get('roles', {})
        return roles.get(role_id)

    @staticmethod
    def get_layer_preset(organisation, layer_id: str) -> Optional[dict]:
        """
        Get a specific layer preset.

        Args:
            organisation: The organisation
            layer_id: The layer identifier (e.g., 'business', 'application')

        Returns:
            dict or None: The layer preset if found
        """
        presets = GraphPresetService.get_presets(organisation)
        layers = presets.get('layers', {})
        return layers.get(layer_id)

    @staticmethod
    def get_concept_ids_for_preset(model: OModel, role_id: str = None, layer_ids: list = None) -> list:
        """
        Get concept IDs that match a preset configuration.

        Args:
            model: The OModel to search in
            role_id: Optional role preset to apply
            layer_ids: Optional list of layer presets to apply

        Returns:
            list: List of matching concept IDs
        """
        presets = GraphPresetService.get_presets(model.organisation)
        concept_names = set()

        # Collect concept names from role preset
        if role_id:
            role = presets.get('roles', {}).get(role_id, {})
            concept_names.update(role.get('default_concepts', []))

        # Collect concept names from layer presets
        if layer_ids:
            for layer_id in layer_ids:
                layer = presets.get('layers', {}).get(layer_id, {})
                concept_names.update(layer.get('concepts', []))

        if not concept_names:
            return []

        # Find matching concepts in the model (case-insensitive partial match)
        matching_ids = []
        for concept in OConcept.objects.filter(model=model):
            concept_name_lower = concept.name.lower()
            for name in concept_names:
                if name.lower() in concept_name_lower or concept_name_lower in name.lower():
                    matching_ids.append(str(concept.id))
                    break

        return matching_ids

    @staticmethod
    def get_relation_ids_for_preset(model: OModel, role_id: str = None) -> list:
        """
        Get relation IDs that match a preset configuration.

        Args:
            model: The OModel to search in
            role_id: The role preset to apply

        Returns:
            list: List of matching relation IDs
        """
        if not role_id:
            return []

        presets = GraphPresetService.get_presets(model.organisation)
        role = presets.get('roles', {}).get(role_id, {})
        relation_names = set(role.get('default_relations', []))

        if not relation_names:
            return []

        # Find matching relations in the model (case-insensitive partial match)
        matching_ids = []
        for relation in ORelation.objects.filter(model=model):
            relation_name_lower = relation.name.lower()
            for name in relation_names:
                if name.lower() in relation_name_lower or relation_name_lower in name.lower():
                    matching_ids.append(str(relation.id))
                    break

        return matching_ids

    @staticmethod
    def get_org_units(model: OModel) -> list:
        """
        Get organizational units from the model for scope filtering.
        Looks for instances of organizational unit concepts using various naming patterns.

        Args:
            model: The OModel to search in

        Returns:
            list: List of org unit dicts with id, name, code, and level
        """
        presets = GraphPresetService.get_presets(model.organisation)
        org_config = presets.get('org_unit_config', {})
        concept_name = org_config.get('concept_name', 'Organisation Unit')

        # Try multiple naming patterns for org unit concepts
        org_unit_patterns = [
            concept_name,
            'Organisation',
            'Organization',
            'OrganisationUnit',
            'OrganizationUnit',
            'Org Unit',
            'OrgUnit',
            'Department',
            'Agency',
            'Ministry',
            'Unit',
        ]

        org_unit_concepts = []
        for pattern in org_unit_patterns:
            concepts = OConcept.objects.filter(
                model=model,
                name__icontains=pattern,
                native=False  # Exclude native/system concepts
            )
            for c in concepts:
                if c not in org_unit_concepts:
                    org_unit_concepts.append(c)

        if not org_unit_concepts:
            return []

        # Get all instances of Organisation Unit concepts
        org_units = []
        seen_ids = set()
        for concept in org_unit_concepts:
            for instance in OInstance.objects.filter(concept=concept).order_by('name'):
                if str(instance.id) not in seen_ids:
                    seen_ids.add(str(instance.id))
                    org_units.append({
                        'id': str(instance.id),
                        'name': instance.name,
                        'code': instance.code or '',
                        'concept': concept.name,
                        'level': 0  # TODO: Calculate hierarchy level from parent relationships
                    })

        return org_units

    @staticmethod
    def get_instances_by_org_unit(model: OModel, org_unit_id: str, include_children: bool = True) -> list:
        """
        Get instance IDs that are owned by a specific organizational unit.
        Checks multiple ownership patterns:
        - Instance "ownedBy" OrgUnit
        - OrgUnit "owns" Instance

        Args:
            model: The OModel to search in
            org_unit_id: The ID of the organizational unit
            include_children: Whether to include instances owned by child org units

        Returns:
            list: List of instance IDs owned by the org unit
        """
        presets = GraphPresetService.get_presets(model.organisation)
        org_config = presets.get('org_unit_config', {})
        ownership_relation = org_config.get('ownership_relation', 'ownedBy')

        try:
            org_unit = OInstance.objects.get(id=org_unit_id)
        except OInstance.DoesNotExist:
            return []

        owned_instance_ids = set()

        # Pattern 1: Instance "ownedBy" OrgUnit (instance is subject, org unit is object)
        slots_owned_by = OSlot.objects.filter(
            model=model,
            object=org_unit,
            predicate__relation__name__icontains=ownership_relation
        ).select_related('subject')

        for slot in slots_owned_by:
            if slot.subject:
                owned_instance_ids.add(str(slot.subject.id))

        # Pattern 2: OrgUnit "owns" Instance (org unit is subject, instance is object)
        # Also check for "manages", "responsible-for" relationships
        ownership_patterns = ['owns', 'manages', 'responsible']
        for pattern in ownership_patterns:
            slots_owns = OSlot.objects.filter(
                model=model,
                subject=org_unit,
                predicate__relation__name__icontains=pattern
            ).select_related('object')

            for slot in slots_owns:
                if slot.object:
                    owned_instance_ids.add(str(slot.object.id))

        if include_children:
            # Get ALL subordinate org units recursively
            all_subordinates = GraphPresetService._get_all_subordinate_units(model, org_unit)
            for subordinate in all_subordinates:
                subordinate_owned = GraphPresetService.get_instances_by_org_unit(
                    model, str(subordinate.id), include_children=False
                )
                owned_instance_ids.update(subordinate_owned)

        return list(owned_instance_ids)

    @staticmethod
    def _get_all_subordinate_units(model: OModel, parent_org_unit: OInstance, visited: set = None) -> list:
        """
        Recursively get ALL subordinate organizational units.

        Args:
            model: The OModel
            parent_org_unit: The parent org unit instance
            visited: Set of already visited org unit IDs to prevent infinite loops

        Returns:
            list: List of all subordinate OInstance objects
        """
        if visited is None:
            visited = set()

        if parent_org_unit.id in visited:
            return []

        visited.add(parent_org_unit.id)

        direct_children = GraphPresetService._get_child_org_units(model, parent_org_unit)
        all_subordinates = list(direct_children)

        # Recursively get subordinates of each child
        for child in direct_children:
            grandchildren = GraphPresetService._get_all_subordinate_units(model, child, visited)
            all_subordinates.extend(grandchildren)

        return all_subordinates

    @staticmethod
    def _get_child_org_units(model: OModel, parent_org_unit: OInstance) -> list:
        """
        Get child organizational units of a parent org unit.
        Checks multiple relationship patterns:
        - Child "reports-to" / "part-of" / "belongs-to" Parent (child is subject, parent is object)
        - Parent "contains" / "has" Child (parent is subject, child is object)

        Args:
            model: The OModel
            parent_org_unit: The parent org unit instance

        Returns:
            list: List of child OInstance objects
        """
        from django.db.models import Q

        children = []
        seen_ids = {parent_org_unit.id}  # Exclude parent from results

        # Pattern 1: Child points to Parent (child is subject, parent is object)
        # ONLY for "reports-to", "part-of", "belongs-to" type relationships (NOT "contains")
        child_to_parent_relations = ['reports', 'part-of', 'belongs', 'subordinate', 'member']
        child_to_parent_slots = OSlot.objects.filter(
            model=model,
            object=parent_org_unit,
            subject__concept__name__icontains='Organisation'
        ).select_related('subject', 'predicate__relation')

        for slot in child_to_parent_slots:
            # Skip if this is a "contains" type relationship (parent contains child)
            relation_name = slot.predicate.relation.name.lower()
            is_child_to_parent = any(r in relation_name for r in child_to_parent_relations)
            if is_child_to_parent and slot.subject and slot.subject.id not in seen_ids:
                seen_ids.add(slot.subject.id)
                children.append(slot.subject)

        # Pattern 2: Parent points to Child (parent is subject, child is object)
        # For "contains", "has-department", "has-unit", "includes" type relationships
        parent_to_child_relations = ['contains', 'has', 'includes', 'comprises']
        parent_to_child_slots = OSlot.objects.filter(
            model=model,
            subject=parent_org_unit,
            object__concept__name__icontains='Organisation'
        ).select_related('object', 'predicate__relation')

        for slot in parent_to_child_slots:
            relation_name = slot.predicate.relation.name.lower()
            is_parent_to_child = any(r in relation_name for r in parent_to_child_relations)
            if is_parent_to_child and slot.object and slot.object.id not in seen_ids:
                seen_ids.add(slot.object.id)
                children.append(slot.object)

        return children

    @staticmethod
    def reset_to_defaults(organisation) -> Configuration:
        """
        Reset presets to defaults for an organisation.

        Args:
            organisation: The organisation to reset

        Returns:
            Configuration: The reset configuration object
        """
        return GraphPresetService.save_presets(organisation, DEFAULT_PRESETS)

    @staticmethod
    def add_role(organisation, role_id: str, role_config: dict) -> dict:
        """
        Add or update a role preset.

        Args:
            organisation: The organisation
            role_id: The role identifier
            role_config: The role configuration

        Returns:
            dict: Updated presets
        """
        presets = GraphPresetService.get_presets(organisation)
        if 'roles' not in presets:
            presets['roles'] = {}
        presets['roles'][role_id] = role_config
        GraphPresetService.save_presets(organisation, presets)
        return presets

    @staticmethod
    def remove_role(organisation, role_id: str) -> dict:
        """
        Remove a role preset.

        Args:
            organisation: The organisation
            role_id: The role identifier to remove

        Returns:
            dict: Updated presets
        """
        presets = GraphPresetService.get_presets(organisation)
        if 'roles' in presets and role_id in presets['roles']:
            del presets['roles'][role_id]
            GraphPresetService.save_presets(organisation, presets)
        return presets

    @staticmethod
    def add_layer(organisation, layer_id: str, layer_config: dict) -> dict:
        """
        Add or update a layer preset.

        Args:
            organisation: The organisation
            layer_id: The layer identifier
            layer_config: The layer configuration

        Returns:
            dict: Updated presets
        """
        presets = GraphPresetService.get_presets(organisation)
        if 'layers' not in presets:
            presets['layers'] = {}
        presets['layers'][layer_id] = layer_config
        GraphPresetService.save_presets(organisation, presets)
        return presets

    @staticmethod
    def map_concept_to_layer(organisation, concept_name: str, layer_id: str) -> dict:
        """
        Map a concept to a layer.

        Args:
            organisation: The organisation
            concept_name: The concept name to map
            layer_id: The layer to map to

        Returns:
            dict: Updated presets
        """
        presets = GraphPresetService.get_presets(organisation)
        if 'layers' not in presets:
            presets['layers'] = {}
        if layer_id not in presets['layers']:
            presets['layers'][layer_id] = {'concepts': []}
        if 'concepts' not in presets['layers'][layer_id]:
            presets['layers'][layer_id]['concepts'] = []

        if concept_name not in presets['layers'][layer_id]['concepts']:
            presets['layers'][layer_id]['concepts'].append(concept_name)

        GraphPresetService.save_presets(organisation, presets)
        return presets

    @staticmethod
    def get_connected_instances(model: OModel, source_instance_ids: list, target_concept_ids: list = None) -> list:
        """
        Get instances connected to source instances via any relationship.
        This enables transitive filtering: when filtering by org unit + non-Application layer,
        first find Applications owned by org unit, then find items connected to those Applications.

        Args:
            model: The OModel
            source_instance_ids: List of instance IDs to find connections from
            target_concept_ids: Optional list of concept IDs to filter results

        Returns:
            list: List of connected instance IDs
        """
        connected_ids = set()

        if not source_instance_ids:
            return []

        # Convert string IDs to proper format for query
        source_ids = [str(sid) for sid in source_instance_ids]

        # Find slots where source is subject → get objects
        slots_as_subject = OSlot.objects.filter(
            model=model,
            subject__id__in=source_ids
        ).select_related('object', 'object__concept')

        for slot in slots_as_subject:
            if slot.object:
                if target_concept_ids is None or str(slot.object.concept.id) in target_concept_ids:
                    connected_ids.add(str(slot.object.id))

        # Find slots where source is object → get subjects
        slots_as_object = OSlot.objects.filter(
            model=model,
            object__id__in=source_ids
        ).select_related('subject', 'subject__concept')

        for slot in slots_as_object:
            if slot.subject:
                if target_concept_ids is None or str(slot.subject.concept.id) in target_concept_ids:
                    connected_ids.add(str(slot.subject.id))

        return list(connected_ids)

    @staticmethod
    def get_application_concept_ids(model: OModel) -> list:
        """
        Get concept IDs that are likely Application-layer concepts.

        Args:
            model: The OModel

        Returns:
            list: List of Application concept IDs
        """
        app_keywords = ['application', 'app', 'system', 'software']
        app_concept_ids = []

        for concept in OConcept.objects.filter(model=model, native=False):
            concept_name_lower = concept.name.lower()
            if any(keyword in concept_name_lower for keyword in app_keywords):
                app_concept_ids.append(str(concept.id))

        return app_concept_ids
