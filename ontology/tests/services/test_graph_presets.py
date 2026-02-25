"""
Tests for the GraphPresetService.
"""
import pytest
from django.contrib.auth.models import User

from configuration.models import Configuration
from ontology.models import OModel, OConcept, ORelation, OInstance, OPredicate, OSlot, Repository
from ontology.services.graph_presets import GraphPresetService, DEFAULT_PRESETS, GRAPH_PRESETS_CONFIG_NAME
from organisation.models import Organisation


@pytest.fixture
def organisation(db):
    """Create a test organisation."""
    return Organisation.objects.create(name='Test Organisation')


@pytest.fixture
def user(db, organisation):
    """Create a test user."""
    user = User.objects.create_user(username='testuser', password='testpass')
    return user


@pytest.fixture
def repository(db, organisation):
    """Create a test repository."""
    return Repository.objects.create(
        name='Test Repository',
        organisation=organisation
    )


@pytest.fixture
def model(db, repository, organisation):
    """Create a test model with concepts and relations."""
    model = OModel.objects.create(
        name='Test Model',
        repository=repository,
        organisation=organisation
    )

    # Create some concepts
    OConcept.objects.create(model=model, name='Business Process', organisation=organisation)
    OConcept.objects.create(model=model, name='Capability', organisation=organisation)
    OConcept.objects.create(model=model, name='Application', organisation=organisation)
    OConcept.objects.create(model=model, name='Interface', organisation=organisation)
    OConcept.objects.create(model=model, name='Data Entity', organisation=organisation)
    OConcept.objects.create(model=model, name='Technology', organisation=organisation)
    org_unit_concept = OConcept.objects.create(model=model, name='Organisation Unit', organisation=organisation)

    # Create some relations
    ORelation.objects.create(model=model, name='realizes', organisation=organisation)
    ORelation.objects.create(model=model, name='depends-on', organisation=organisation)
    ORelation.objects.create(model=model, name='uses', organisation=organisation)
    owned_by_relation = ORelation.objects.create(model=model, name='ownedBy', organisation=organisation)

    # Create predicate for ownedBy
    predicate = OPredicate.objects.create(
        model=model,
        organisation=organisation,
        subject=OConcept.objects.get(model=model, name='Application'),
        relation=owned_by_relation,
        object=org_unit_concept
    )

    # Create some org unit instances
    gra = OInstance.objects.create(
        model=model,
        concept=org_unit_concept,
        name='GRA',
        organisation=organisation
    )
    moh = OInstance.objects.create(
        model=model,
        concept=org_unit_concept,
        name='MoH',
        organisation=organisation
    )

    # Create application instances
    app_concept = OConcept.objects.get(model=model, name='Application')
    asycuda = OInstance.objects.create(
        model=model,
        concept=app_concept,
        name='ASYCUDA',
        organisation=organisation
    )
    dhis2 = OInstance.objects.create(
        model=model,
        concept=app_concept,
        name='DHIS2',
        organisation=organisation
    )

    # Create ownedBy slots
    OSlot.objects.create(
        model=model,
        organisation=organisation,
        predicate=predicate,
        subject=asycuda,
        object=gra
    )
    OSlot.objects.create(
        model=model,
        organisation=organisation,
        predicate=predicate,
        subject=dhis2,
        object=moh
    )

    return model


class TestGraphPresetServiceGetPresets:
    """Tests for get_presets method."""

    def test_returns_defaults_when_no_config_exists(self, organisation):
        """Should return default presets when no configuration exists."""
        presets = GraphPresetService.get_presets(organisation)

        assert presets == DEFAULT_PRESETS
        assert 'roles' in presets
        assert 'layers' in presets
        assert 'business_architect' in presets['roles']
        assert 'business' in presets['layers']

    def test_returns_saved_presets(self, organisation):
        """Should return saved presets when configuration exists."""
        custom_presets = {
            'roles': {
                'custom_role': {
                    'display_name': 'Custom Role',
                    'default_concepts': ['Custom Concept'],
                    'default_relations': ['custom-relation']
                }
            },
            'layers': {}
        }

        Configuration.objects.create(
            organisation=organisation,
            name=GRAPH_PRESETS_CONFIG_NAME,
            content=custom_presets
        )

        presets = GraphPresetService.get_presets(organisation)

        assert presets == custom_presets
        assert 'custom_role' in presets['roles']


class TestGraphPresetServiceSavePresets:
    """Tests for save_presets method."""

    def test_creates_new_config(self, organisation):
        """Should create new configuration when none exists."""
        custom_presets = {'roles': {'test': {}}, 'layers': {}}

        config = GraphPresetService.save_presets(organisation, custom_presets)

        assert config.content == custom_presets
        assert config.organisation == organisation

    def test_updates_existing_config(self, organisation):
        """Should update existing configuration."""
        # Create initial config
        Configuration.objects.create(
            organisation=organisation,
            name=GRAPH_PRESETS_CONFIG_NAME,
            content={'roles': {}, 'layers': {}}
        )

        new_presets = {'roles': {'new_role': {}}, 'layers': {}}
        config = GraphPresetService.save_presets(organisation, new_presets)

        assert config.content == new_presets


class TestGraphPresetServiceGetRolePreset:
    """Tests for get_role_preset method."""

    def test_returns_role_preset(self, organisation):
        """Should return specific role preset."""
        role = GraphPresetService.get_role_preset(organisation, 'business_architect')

        assert role is not None
        assert 'display_name' in role
        assert 'default_concepts' in role
        assert 'default_relations' in role

    def test_returns_none_for_unknown_role(self, organisation):
        """Should return None for unknown role."""
        role = GraphPresetService.get_role_preset(organisation, 'nonexistent_role')

        assert role is None


class TestGraphPresetServiceGetConceptIdsForPreset:
    """Tests for get_concept_ids_for_preset method."""

    def test_returns_matching_concepts_for_role(self, model):
        """Should return concept IDs matching the role preset."""
        concept_ids = GraphPresetService.get_concept_ids_for_preset(
            model,
            role_id='business_architect'
        )

        # Should match Business Process and Capability
        assert len(concept_ids) >= 1
        business_process = OConcept.objects.get(model=model, name='Business Process')
        assert str(business_process.id) in concept_ids

    def test_returns_matching_concepts_for_layers(self, model):
        """Should return concept IDs matching the layer presets."""
        concept_ids = GraphPresetService.get_concept_ids_for_preset(
            model,
            layer_ids=['business', 'application']
        )

        # Should match concepts from both layers
        assert len(concept_ids) >= 2

    def test_returns_empty_list_when_no_matches(self, model):
        """Should return empty list when no concepts match."""
        # Create custom preset with non-matching concepts
        custom_presets = {
            'roles': {
                'test_role': {
                    'default_concepts': ['Nonexistent Concept'],
                    'default_relations': []
                }
            },
            'layers': {}
        }
        GraphPresetService.save_presets(model.organisation, custom_presets)

        concept_ids = GraphPresetService.get_concept_ids_for_preset(
            model,
            role_id='test_role'
        )

        assert concept_ids == []


class TestGraphPresetServiceGetRelationIdsForPreset:
    """Tests for get_relation_ids_for_preset method."""

    def test_returns_matching_relations(self, model):
        """Should return relation IDs matching the role preset."""
        relation_ids = GraphPresetService.get_relation_ids_for_preset(
            model,
            role_id='business_architect'
        )

        # Should match 'realizes' relation
        realizes = ORelation.objects.get(model=model, name='realizes')
        assert str(realizes.id) in relation_ids

    def test_returns_empty_list_when_no_role(self, model):
        """Should return empty list when no role specified."""
        relation_ids = GraphPresetService.get_relation_ids_for_preset(model, role_id=None)

        assert relation_ids == []


class TestGraphPresetServiceGetOrgUnits:
    """Tests for get_org_units method."""

    def test_returns_org_units(self, model):
        """Should return organizational units from the model."""
        org_units = GraphPresetService.get_org_units(model)

        assert len(org_units) == 2
        names = [ou['name'] for ou in org_units]
        assert 'GRA' in names
        assert 'MoH' in names

    def test_returns_empty_list_when_no_org_units(self, repository, organisation):
        """Should return empty list when no org units exist."""
        empty_model = OModel.objects.create(
            name='Empty Model',
            repository=repository,
            organisation=organisation
        )

        org_units = GraphPresetService.get_org_units(empty_model)

        assert org_units == []


class TestGraphPresetServiceGetInstancesByOrgUnit:
    """Tests for get_instances_by_org_unit method."""

    def test_returns_instances_owned_by_org_unit(self, model):
        """Should return instances owned by the org unit."""
        gra = OInstance.objects.get(model=model, name='GRA')

        instance_ids = GraphPresetService.get_instances_by_org_unit(
            model,
            str(gra.id)
        )

        # Should include ASYCUDA (owned by GRA)
        asycuda = OInstance.objects.get(model=model, name='ASYCUDA')
        assert str(asycuda.id) in instance_ids

        # Should not include DHIS2 (owned by MoH)
        dhis2 = OInstance.objects.get(model=model, name='DHIS2')
        assert str(dhis2.id) not in instance_ids

    def test_returns_empty_list_for_unknown_org_unit(self, model):
        """Should return empty list for non-existent org unit."""
        import uuid
        instance_ids = GraphPresetService.get_instances_by_org_unit(
            model,
            str(uuid.uuid4())
        )

        assert instance_ids == []


class TestGraphPresetServiceResetToDefaults:
    """Tests for reset_to_defaults method."""

    def test_resets_to_defaults(self, organisation):
        """Should reset presets to default values."""
        # Save custom presets
        custom_presets = {'roles': {'custom': {}}, 'layers': {}}
        GraphPresetService.save_presets(organisation, custom_presets)

        # Reset to defaults
        GraphPresetService.reset_to_defaults(organisation)

        presets = GraphPresetService.get_presets(organisation)
        assert presets == DEFAULT_PRESETS


class TestGraphPresetServiceAddRole:
    """Tests for add_role method."""

    def test_adds_new_role(self, organisation):
        """Should add a new role to presets."""
        role_config = {
            'display_name': 'Test Role',
            'default_concepts': ['Test Concept'],
            'default_relations': ['test-relation']
        }

        presets = GraphPresetService.add_role(organisation, 'test_role', role_config)

        assert 'test_role' in presets['roles']
        assert presets['roles']['test_role'] == role_config


class TestGraphPresetServiceRemoveRole:
    """Tests for remove_role method."""

    def test_removes_existing_role(self, organisation):
        """Should remove an existing role from presets."""
        # First add a role
        GraphPresetService.add_role(organisation, 'test_role', {'display_name': 'Test'})

        # Then remove it
        presets = GraphPresetService.remove_role(organisation, 'test_role')

        assert 'test_role' not in presets['roles']


class TestGraphPresetServiceMapConceptToLayer:
    """Tests for map_concept_to_layer method."""

    def test_maps_concept_to_layer(self, organisation):
        """Should map a concept to a layer."""
        presets = GraphPresetService.map_concept_to_layer(
            organisation,
            'New Concept',
            'business'
        )

        assert 'New Concept' in presets['layers']['business']['concepts']

    def test_does_not_duplicate_concepts(self, organisation):
        """Should not duplicate concept mappings."""
        GraphPresetService.map_concept_to_layer(organisation, 'Test', 'business')
        presets = GraphPresetService.map_concept_to_layer(organisation, 'Test', 'business')

        count = presets['layers']['business']['concepts'].count('Test')
        assert count == 1


@pytest.fixture
def model_with_data_entities(db, repository, organisation):
    """Create a test model with Applications, DataEntities, and connections."""
    model = OModel.objects.create(
        name='Test Model With Data',
        repository=repository,
        organisation=organisation
    )

    # Create concepts
    app_concept = OConcept.objects.create(model=model, name='Application', organisation=organisation)
    data_concept = OConcept.objects.create(model=model, name='DataEntity', organisation=organisation)
    org_unit_concept = OConcept.objects.create(model=model, name='Organisation Unit', organisation=organisation)

    # Create relations
    owned_by_relation = ORelation.objects.create(model=model, name='ownedBy', organisation=organisation)
    uses_relation = ORelation.objects.create(model=model, name='uses', organisation=organisation)

    # Create predicates
    app_owned_by_pred = OPredicate.objects.create(
        model=model, organisation=organisation,
        subject=app_concept, relation=owned_by_relation, object=org_unit_concept
    )
    app_uses_data_pred = OPredicate.objects.create(
        model=model, organisation=organisation,
        subject=app_concept, relation=uses_relation, object=data_concept
    )

    # Create org unit instance
    minfin = OInstance.objects.create(
        model=model, concept=org_unit_concept, name='MinFin', organisation=organisation
    )

    # Create application instances
    ifmis = OInstance.objects.create(
        model=model, concept=app_concept, name='IFMIS', organisation=organisation
    )
    gampay = OInstance.objects.create(
        model=model, concept=app_concept, name='GamPay', organisation=organisation
    )

    # Create data entity instances
    financial_tx = OInstance.objects.create(
        model=model, concept=data_concept, name='Financial Transaction', organisation=organisation
    )
    payment_tx = OInstance.objects.create(
        model=model, concept=data_concept, name='Payment Transaction', organisation=organisation
    )
    unrelated_data = OInstance.objects.create(
        model=model, concept=data_concept, name='Unrelated Data', organisation=organisation
    )

    # Create ownership slots (IFMIS and GamPay owned by MinFin)
    OSlot.objects.create(
        model=model, organisation=organisation,
        predicate=app_owned_by_pred, subject=ifmis, object=minfin
    )
    OSlot.objects.create(
        model=model, organisation=organisation,
        predicate=app_owned_by_pred, subject=gampay, object=minfin
    )

    # Create uses slots (IFMIS uses Financial Transaction, GamPay uses Payment Transaction)
    OSlot.objects.create(
        model=model, organisation=organisation,
        predicate=app_uses_data_pred, subject=ifmis, object=financial_tx
    )
    OSlot.objects.create(
        model=model, organisation=organisation,
        predicate=app_uses_data_pred, subject=gampay, object=payment_tx
    )

    return model


class TestGraphPresetServiceGetConnectedInstances:
    """Tests for get_connected_instances method (transitive filtering)."""

    def test_returns_connected_instances(self, model_with_data_entities):
        """Should return instances connected to source instances."""
        model = model_with_data_entities
        ifmis = OInstance.objects.get(model=model, name='IFMIS')

        connected_ids = GraphPresetService.get_connected_instances(
            model, [str(ifmis.id)]
        )

        # Should include Financial Transaction (connected via uses)
        financial_tx = OInstance.objects.get(model=model, name='Financial Transaction')
        assert str(financial_tx.id) in connected_ids

        # Should include MinFin (connected via ownedBy)
        minfin = OInstance.objects.get(model=model, name='MinFin')
        assert str(minfin.id) in connected_ids

    def test_filters_by_target_concepts(self, model_with_data_entities):
        """Should filter connected instances by target concept IDs."""
        model = model_with_data_entities
        ifmis = OInstance.objects.get(model=model, name='IFMIS')
        data_concept = OConcept.objects.get(model=model, name='DataEntity')

        connected_ids = GraphPresetService.get_connected_instances(
            model, [str(ifmis.id)], target_concept_ids=[str(data_concept.id)]
        )

        # Should include Financial Transaction (DataEntity)
        financial_tx = OInstance.objects.get(model=model, name='Financial Transaction')
        assert str(financial_tx.id) in connected_ids

        # Should NOT include MinFin (Organisation Unit, not DataEntity)
        minfin = OInstance.objects.get(model=model, name='MinFin')
        assert str(minfin.id) not in connected_ids

    def test_returns_empty_for_no_connections(self, model_with_data_entities):
        """Should return empty list when no connections exist."""
        model = model_with_data_entities
        unrelated = OInstance.objects.get(model=model, name='Unrelated Data')

        connected_ids = GraphPresetService.get_connected_instances(
            model, [str(unrelated.id)]
        )

        # Unrelated Data has no connections
        assert len(connected_ids) == 0

    def test_returns_empty_for_empty_source(self, model_with_data_entities):
        """Should return empty list when source list is empty."""
        model = model_with_data_entities

        connected_ids = GraphPresetService.get_connected_instances(model, [])

        assert connected_ids == []

    def test_handles_multiple_source_instances(self, model_with_data_entities):
        """Should return connections from multiple source instances."""
        model = model_with_data_entities
        ifmis = OInstance.objects.get(model=model, name='IFMIS')
        gampay = OInstance.objects.get(model=model, name='GamPay')
        data_concept = OConcept.objects.get(model=model, name='DataEntity')

        connected_ids = GraphPresetService.get_connected_instances(
            model, [str(ifmis.id), str(gampay.id)], target_concept_ids=[str(data_concept.id)]
        )

        # Should include both Financial Transaction and Payment Transaction
        financial_tx = OInstance.objects.get(model=model, name='Financial Transaction')
        payment_tx = OInstance.objects.get(model=model, name='Payment Transaction')
        assert str(financial_tx.id) in connected_ids
        assert str(payment_tx.id) in connected_ids


class TestGraphPresetServiceGetApplicationConceptIds:
    """Tests for get_application_concept_ids method."""

    def test_returns_application_concepts(self, model_with_data_entities):
        """Should return concept IDs for Application-like concepts."""
        model = model_with_data_entities

        app_ids = GraphPresetService.get_application_concept_ids(model)

        app_concept = OConcept.objects.get(model=model, name='Application')
        assert str(app_concept.id) in app_ids

    def test_does_not_return_non_application_concepts(self, model_with_data_entities):
        """Should not return non-Application concept IDs."""
        model = model_with_data_entities

        app_ids = GraphPresetService.get_application_concept_ids(model)

        data_concept = OConcept.objects.get(model=model, name='DataEntity')
        assert str(data_concept.id) not in app_ids
