import json

from django.test import TestCase
from django.urls import reverse

from ontology.models import OConcept, OInstance, OModel, OPredicate, ORelation, OSlot
from utils.test.helpers import (
    add_object_type_accesspermissions_to_security_group,
    populate_test_env,
)


class OModelPathFinderTestCase(TestCase):
    def setUp(self):
        populate_test_env(self)
        # Add all required permissions for pathfinder
        for object_type in [OModel.get_object_type(), OConcept.get_object_type(),
                           ORelation.get_object_type(), OPredicate.get_object_type(),
                           OInstance.get_object_type(), OSlot.get_object_type()]:
            add_object_type_accesspermissions_to_security_group(
                organisation=self.org_1,
                security_group=self.org_1_security_group_1,
                object_type=object_type
            )

    def _login_and_activate_profile(self):
        """Helper to login and activate profile."""
        logged_in = self.client.login(username='org_1_user_1', password='12345')
        self.assertTrue(logged_in)
        response = self.client.post(
            reverse('profile_activate', kwargs={'pk': str(self.org_1_user_1_profile.id)})
        )
        self.assertEqual(response.status_code, 302)

    def test_pathfinder_not_authenticated(self):
        """Test that unauthenticated users are redirected to login."""
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_instance_id': str(self.org_1_instance_3.id),
            'find_all_of_concept': False
        }), content_type='application/json')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_pathfinder_single_instance_mode(self):
        """Test single-instance path finding via API (regression test)."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        # Test path between connected instances
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_instance_id': str(self.org_1_instance_3.id),
            'find_all_of_concept': False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)  # Should find at least one path
        # Path should have slots
        self.assertTrue(len(data[0]) > 0)

    def test_pathfinder_single_instance_no_path(self):
        """Test single-instance mode when no path exists."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        # instance_8 is not connected to instance_1
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_instance_id': str(self.org_1_instance_8.id),
            'find_all_of_concept': False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)  # No path found

    def test_pathfinder_multi_target_mode(self):
        """Test multi-target path finding via API."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_concept_id': str(self.org_1_concept_2.id),
            'find_all_of_concept': True
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        # Check response structure
        self.assertIn('paths', data)
        self.assertIn('target_instances', data)
        self.assertIn('truncated', data)
        self.assertIn('total_found', data)
        self.assertIn('concept_name', data)

        # concept_2 has instances: instance_2, instance_6
        self.assertEqual(data['concept_name'], 'org_1_concept_2')

    def test_pathfinder_multi_target_with_max_results(self):
        """Test max_results parameter in multi-target mode."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_concept_id': str(self.org_1_concept_2.id),
            'find_all_of_concept': True,
            'max_results': 1
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        # Should only have 1 path entry (max_results=1)
        self.assertLessEqual(len(data['paths']), 1)

    def test_pathfinder_multi_target_finds_connected_and_unconnected(self):
        """Test that multi-target mode correctly identifies connected vs unconnected instances."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        # concept_2 has instance_2 (connected to instance_1) and instance_6 (not connected)
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_concept_id': str(self.org_1_concept_2.id),
            'find_all_of_concept': True
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        # instance_2 should have a path (connected)
        instance_2_path = data['paths'].get(str(self.org_1_instance_2.id))
        self.assertIsNotNone(instance_2_path)
        self.assertIsInstance(instance_2_path, list)
        self.assertTrue(len(instance_2_path) > 0)

        # instance_6 should have None (not connected)
        instance_6_path = data['paths'].get(str(self.org_1_instance_6.id))
        self.assertIsNone(instance_6_path)

    def test_pathfinder_excludes_start_instance(self):
        """Test that start instance is excluded from target instances."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        # Search for instances of concept_1 starting from instance_1 (which is also concept_1)
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_concept_id': str(self.org_1_concept_1.id),
            'find_all_of_concept': True
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        # Start instance should not be in target_instances
        self.assertNotIn(str(self.org_1_instance_1.id), data['target_instances'])

    def test_pathfinder_with_relation_filter(self):
        """Test single-instance path finding with relation filter."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        # instance_1 -> instance_2 uses relation_1
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_instance_id': str(self.org_1_instance_2.id),
            'relation_ids': [str(self.org_1_relation_1.id)],
            'find_all_of_concept': False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)  # Should find path via relation_1

    def test_pathfinder_with_non_matching_relation_filter(self):
        """Test that non-matching relation filter returns no paths."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        # instance_1 -> instance_2 uses relation_1, but we filter for relation_3
        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_instance_id': str(self.org_1_instance_2.id),
            'relation_ids': [str(self.org_1_relation_3.id)],
            'find_all_of_concept': False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)  # No path via relation_3

    def test_pathfinder_multi_target_with_relation_filter(self):
        """Test multi-target path finding with relation filter."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_concept_id': str(self.org_1_concept_2.id),
            'relation_ids': [str(self.org_1_relation_1.id)],
            'find_all_of_concept': True
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('paths', data)

        # instance_2 is connected via relation_1
        instance_2_path = data['paths'].get(str(self.org_1_instance_2.id))
        self.assertIsNotNone(instance_2_path)
        self.assertIsInstance(instance_2_path, list)

    def test_pathfinder_empty_relation_filter_finds_all(self):
        """Test that empty relation_ids list finds all paths (same as no filter)."""
        self._login_and_activate_profile()
        url = reverse('o_model_pathfinder', kwargs={'model_id': self.org_1_model_1.id})

        response = self.client.post(url, data=json.dumps({
            'start_instance_id': str(self.org_1_instance_1.id),
            'end_instance_id': str(self.org_1_instance_2.id),
            'relation_ids': [],  # Empty list
            'find_all_of_concept': False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(len(data) > 0)  # Should find path
