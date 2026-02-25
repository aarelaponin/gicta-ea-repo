"""
Tests for the OModel presets views.
"""
import json
from django.test import TestCase
from django.urls import reverse

from ontology.models import OModel, OConcept, ORelation, OInstance, OPredicate, OSlot
from ontology.services.graph_presets import GraphPresetService
from utils.test.helpers import (
    add_object_type_accesspermissions_to_security_group,
    create_accesspermission,
    create_organisation,
    create_repository,
    create_security_group,
    create_user,
    create_user_profile,
    create_model,
    create_concept,
    create_relation,
    create_instance,
)


class OModelPresetsViewTestCase(TestCase):
    """Tests for the presets API endpoint."""

    def setUp(self):
        self.org_1 = create_organisation(name='Org 1', description='', location='test')
        self.org_1_user_1 = create_user(username='org_1_user_1')
        self.org_1_user_1_profile = create_user_profile(role='Admin', user=self.org_1_user_1, organisation=self.org_1)
        self.org_1_security_group_1 = create_security_group(name='Org 1 SecG 1', description='', organisation=self.org_1)
        self.org_1_security_group_1.profiles.add(self.org_1_user_1_profile)
        self.object_type = OModel.get_object_type()
        add_object_type_accesspermissions_to_security_group(
            organisation=self.org_1,
            security_group=self.org_1_security_group_1,
            object_type=self.object_type
        )

        self.org_1_repo_1 = create_repository(organisation=self.org_1, name='org_1_repo_1')
        self.org_1_model_1 = create_model(repository=self.org_1_repo_1, name='org_1_model_1')

        # Create some concepts
        self.org_1_concept_1 = create_concept(model=self.org_1_model_1, name='Business Process')
        self.org_1_concept_2 = create_concept(model=self.org_1_model_1, name='Application')
        self.org_1_concept_ou = create_concept(model=self.org_1_model_1, name='Organisation Unit')

        # Create relation
        self.org_1_relation_1 = create_relation(model=self.org_1_model_1, name='ownedBy')

        # Create org unit instance
        self.org_1_ou_gra = create_instance(model=self.org_1_model_1, concept=self.org_1_concept_ou, name='GRA')

    def _login_and_activate_profile(self):
        """Helper to login and activate the user profile."""
        logged_in = self.client.login(username='org_1_user_1', password='12345')
        self.assertTrue(logged_in)
        response = self.client.post(reverse('profile_activate', kwargs={'pk': str(self.org_1_user_1_profile.id)}))
        self.assertEqual(response.status_code, 302)
        create_accesspermission(security_group=self.org_1_security_group_1, action='VIEW', object_type=self.object_type)

    def test_get_presets_not_authenticated(self):
        """Should redirect to login when not authenticated."""
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/presets/')
        self.assertEqual(response.status_code, 302)

    def test_get_presets_authenticated_no_permission(self):
        """Should return 403 when authenticated but no permission."""
        logged_in = self.client.login(username='org_1_user_1', password='12345')
        self.assertTrue(logged_in)
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/presets/')
        self.assertEqual(response.status_code, 403)

    def test_get_presets_returns_json(self):
        """Should return presets as JSON when authenticated with permission."""
        self._login_and_activate_profile()
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/presets/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('roles', data)
        self.assertIn('layers', data)

    def test_get_presets_returns_default_roles(self):
        """Should return default architect roles."""
        self._login_and_activate_profile()
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/presets/')

        data = response.json()
        self.assertIn('business_architect', data['roles'])
        self.assertIn('application_architect', data['roles'])
        self.assertIn('data_architect', data['roles'])
        self.assertIn('technology_architect', data['roles'])

    def test_get_presets_returns_default_layers(self):
        """Should return default BDAT layers."""
        self._login_and_activate_profile()
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/presets/')

        data = response.json()
        self.assertIn('business', data['layers'])
        self.assertIn('application', data['layers'])
        self.assertIn('data', data['layers'])
        self.assertIn('technology', data['layers'])


class OModelOrgUnitsViewTestCase(TestCase):
    """Tests for the org units API endpoint."""

    def setUp(self):
        self.org_1 = create_organisation(name='Org 1', description='', location='test')
        self.org_1_user_1 = create_user(username='org_1_user_1')
        self.org_1_user_1_profile = create_user_profile(role='Admin', user=self.org_1_user_1, organisation=self.org_1)
        self.org_1_security_group_1 = create_security_group(name='Org 1 SecG 1', description='', organisation=self.org_1)
        self.org_1_security_group_1.profiles.add(self.org_1_user_1_profile)
        self.object_type = OModel.get_object_type()
        add_object_type_accesspermissions_to_security_group(
            organisation=self.org_1,
            security_group=self.org_1_security_group_1,
            object_type=self.object_type
        )

        self.org_1_repo_1 = create_repository(organisation=self.org_1, name='org_1_repo_1')
        self.org_1_model_1 = create_model(repository=self.org_1_repo_1, name='org_1_model_1')

        # Create Organisation Unit concept and instances
        self.org_1_concept_ou = create_concept(model=self.org_1_model_1, name='Organisation Unit')
        self.org_1_ou_gra = create_instance(model=self.org_1_model_1, concept=self.org_1_concept_ou, name='GRA')
        self.org_1_ou_moh = create_instance(model=self.org_1_model_1, concept=self.org_1_concept_ou, name='MoH')

    def _login_and_activate_profile(self):
        """Helper to login and activate the user profile."""
        logged_in = self.client.login(username='org_1_user_1', password='12345')
        self.assertTrue(logged_in)
        response = self.client.post(reverse('profile_activate', kwargs={'pk': str(self.org_1_user_1_profile.id)}))
        self.assertEqual(response.status_code, 302)
        create_accesspermission(security_group=self.org_1_security_group_1, action='VIEW', object_type=self.object_type)

    def test_get_org_units_returns_json(self):
        """Should return org units as JSON."""
        self._login_and_activate_profile()
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/org_units/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('org_units', data)

    def test_get_org_units_returns_instances(self):
        """Should return org unit instances."""
        self._login_and_activate_profile()
        response = self.client.get(f'/o_model/{self.org_1_model_1.id}/org_units/')

        data = response.json()
        self.assertEqual(len(data['org_units']), 2)
        names = [ou['name'] for ou in data['org_units']]
        self.assertIn('GRA', names)
        self.assertIn('MoH', names)


class OModelGraphViewWithOrgUnitTestCase(TestCase):
    """Tests for the graph view with org unit filtering."""

    def setUp(self):
        self.org_1 = create_organisation(name='Org 1', description='', location='test')
        self.org_1_user_1 = create_user(username='org_1_user_1')
        self.org_1_user_1_profile = create_user_profile(role='Admin', user=self.org_1_user_1, organisation=self.org_1)
        self.org_1_security_group_1 = create_security_group(name='Org 1 SecG 1', description='', organisation=self.org_1)
        self.org_1_security_group_1.profiles.add(self.org_1_user_1_profile)
        self.object_type = OModel.get_object_type()
        add_object_type_accesspermissions_to_security_group(
            organisation=self.org_1,
            security_group=self.org_1_security_group_1,
            object_type=self.object_type
        )

        self.org_1_repo_1 = create_repository(organisation=self.org_1, name='org_1_repo_1')
        self.org_1_model_1 = create_model(repository=self.org_1_repo_1, name='org_1_model_1')

        # Create concepts
        self.concept_app = create_concept(model=self.org_1_model_1, name='Application')
        self.concept_ou = create_concept(model=self.org_1_model_1, name='Organisation Unit')

        # Create ownedBy relation and predicate
        self.relation_owned_by = create_relation(model=self.org_1_model_1, name='ownedBy')
        self.predicate_app_owned_by = OPredicate.objects.create(
            model=self.org_1_model_1,
            organisation=self.org_1,
            subject=self.concept_app,
            relation=self.relation_owned_by,
            object=self.concept_ou
        )

        # Create org unit instances
        self.org_unit_gra = create_instance(model=self.org_1_model_1, concept=self.concept_ou, name='GRA')

        # Create application instances
        self.app_asycuda = create_instance(model=self.org_1_model_1, concept=self.concept_app, name='ASYCUDA')

        # Create ownedBy slot
        OSlot.objects.create(
            model=self.org_1_model_1,
            organisation=self.org_1,
            predicate=self.predicate_app_owned_by,
            subject=self.app_asycuda,
            object=self.org_unit_gra
        )

    def _login_and_activate_profile(self):
        """Helper to login and activate the user profile."""
        logged_in = self.client.login(username='org_1_user_1', password='12345')
        self.assertTrue(logged_in)
        response = self.client.post(reverse('profile_activate', kwargs={'pk': str(self.org_1_user_1_profile.id)}))
        self.assertEqual(response.status_code, 302)
        create_accesspermission(security_group=self.org_1_security_group_1, action='VIEW', object_type=self.object_type)

    def test_graph_endpoint_exists(self):
        """Should have a graph endpoint that accepts org_unit_id."""
        self._login_and_activate_profile()

        response = self.client.post(
            f'/o_model/graph/{self.org_1_model_1.id}/',
            data=json.dumps({
                'knowledge_set': 'instances',
                'model_id': str(self.org_1_model_1.id),
                'concept_ids': [str(self.concept_app.id)],
                'relation_ids': [str(self.relation_owned_by.id)],
                'predicate_ids': [str(self.predicate_app_owned_by.id)],
                'instance_ids': [str(self.app_asycuda.id)],
                'org_unit_id': str(self.org_unit_gra.id)
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
