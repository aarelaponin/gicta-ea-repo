import os

from django.test import TestCase
from openpyxl import load_workbook

from ontology.controllers.utils import DEFAULT_MAX_LEVEL, KnowledgeBaseUtils
from utils.test.helpers import populate_test_env




class KnowledgeBaseUtilsTestCase(TestCase):
    def setUp(self):
        populate_test_env(self)

    def test_get_parent_concepts(self):
        parent_concepts = KnowledgeBaseUtils.get_parent_concepts(concept=self.org_1_concept_4)
        self.assertEqual(len(parent_concepts), 2, parent_concepts)
        self.assertEqual(parent_concepts[0][0], self.org_1_concept_1, parent_concepts)
        self.assertEqual(parent_concepts[0][1], 0, parent_concepts)
        self.assertEqual(parent_concepts[1][0], self.org_1_concept_0, parent_concepts)
        self.assertEqual(parent_concepts[1][1], 1, parent_concepts)

    def test_get_recursive_parent_concepts(self):
        parent_concepts = KnowledgeBaseUtils.get_recursive_parent_concepts(concept=self.org_1_concept_4, results=[], level=0, max_level=100)
        self.assertEqual(len(parent_concepts), 2, parent_concepts)
        self.assertEqual(parent_concepts[0][0], self.org_1_concept_1, parent_concepts)
        self.assertEqual(parent_concepts[0][1], 0, parent_concepts)
        self.assertEqual(parent_concepts[1][0], self.org_1_concept_0, parent_concepts)
        self.assertEqual(parent_concepts[1][1], 1, parent_concepts) 

    def test_get_child_concepts(self):
        child_concepts = KnowledgeBaseUtils.get_child_concepts(concept=self.org_1_concept_0)
        self.assertEqual(len(child_concepts), 2, child_concepts)
        self.assertEqual(child_concepts[0][0], self.org_1_concept_1, child_concepts)
        self.assertEqual(child_concepts[0][1], 0, child_concepts)
        self.assertEqual(child_concepts[1][0], self.org_1_concept_4, child_concepts)
        self.assertEqual(child_concepts[1][1], 1, child_concepts)

    def test_get_recursive_child_concepts(self):
        child_concepts = KnowledgeBaseUtils.get_recursive_child_concepts(concept=self.org_1_concept_0, results=[], level=0, max_level=100)
        self.assertEqual(len(child_concepts), 2, child_concepts)
        self.assertEqual(child_concepts[0][0], self.org_1_concept_1, child_concepts)
        self.assertEqual(child_concepts[0][1], 0, child_concepts)
        self.assertEqual(child_concepts[1][0], self.org_1_concept_4, child_concepts)
        self.assertEqual(child_concepts[1][1], 1, child_concepts)  


    def test_get_related_object_concepts(self):
        predicate_ids = None
        concepts = KnowledgeBaseUtils.get_related_object_concepts(concept=self.org_1_concept_1, predicate_ids=predicate_ids)
        self.assertEqual(len(concepts), 4, concepts)
        self.assertIn((self.org_1_concept_0, 0), concepts, concepts)
        self.assertIn((self.org_1_concept_3, 1), concepts, concepts)
        concepts = KnowledgeBaseUtils.get_related_object_concepts(concept=self.org_1_concept_1, predicate_ids=predicate_ids, max_level=0)
        self.assertEqual(len(concepts), 3, concepts)
        self.assertIn((self.org_1_concept_0, 0), concepts, concepts)

    def test_get_related_subject_concepts(self):
        predicate_ids = None
        concepts = KnowledgeBaseUtils.get_related_subject_concepts(concept=self.org_1_concept_2, predicate_ids=predicate_ids)
        self.assertEqual(len(concepts), 1, concepts)
        self.assertIn((self.org_1_concept_1, 0), concepts, concepts)

    def test_get_instances_paths(self):
        paths = KnowledgeBaseUtils.get_instances_paths(start_instance=self.org_1_instance_1, end_instance=self.org_1_instance_3)
        best_path = (100, [])
        if not paths.empty():
            best_path = paths.get()
        self.assertEqual(best_path[0], 2, best_path[1])

        paths = KnowledgeBaseUtils.get_instances_paths(start_instance=self.org_1_instance_1, end_instance=self.org_1_instance_8)
        best_path = (100, [])
        if not paths.empty():
            best_path = paths.get()
        self.assertEqual(best_path[0], 100, best_path[1])

        paths = KnowledgeBaseUtils.get_instances_paths(start_instance=self.org_1_instance_0, end_instance=self.org_1_instance_4)
        best_path = (100, [])
        if not paths.empty():
            best_path = paths.get()
        self.assertEqual(best_path[0], 2, best_path[1])

    def test_get_instances_paths_to_multiple_basic(self):
        """Test finding paths to multiple target instances."""
        # instance_1 is connected to instance_2 (1 hop), instance_3 (2 hops via instance_2),
        # instance_4 (1 hop), and instance_0 (1 hop)
        targets = [self.org_1_instance_2, self.org_1_instance_3, self.org_1_instance_4]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets
        )
        self.assertIsInstance(result, dict)
        # Should find paths to all connected instances
        self.assertIn(self.org_1_instance_2.id, result)
        self.assertIn(self.org_1_instance_3.id, result)
        self.assertIn(self.org_1_instance_4.id, result)
        # Check path lengths
        self.assertEqual(len(result[self.org_1_instance_2.id]), 1)  # Direct connection
        self.assertEqual(len(result[self.org_1_instance_3.id]), 2)  # Via instance_2
        self.assertEqual(len(result[self.org_1_instance_4.id]), 1)  # Direct connection

    def test_get_instances_paths_to_multiple_empty_targets(self):
        """Test with empty target list."""
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=[]
        )
        self.assertEqual(result, {})

    def test_get_instances_paths_to_multiple_no_paths(self):
        """Test when no paths exist to any target."""
        # instance_8 is not connected to instance_1
        targets = [self.org_1_instance_8]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets
        )
        # Should not find a path to disconnected instance
        self.assertNotIn(self.org_1_instance_8.id, result)

    def test_get_instances_paths_to_multiple_mixed(self):
        """Test with mix of connected and disconnected targets."""
        # instance_2 is connected, instance_8 is not
        targets = [self.org_1_instance_2, self.org_1_instance_8]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets
        )
        self.assertIn(self.org_1_instance_2.id, result)
        self.assertNotIn(self.org_1_instance_8.id, result)

    def test_get_instances_paths_to_multiple_respects_max_level(self):
        """Test that max_level is respected."""
        # instance_3 requires 2 hops from instance_1
        targets = [self.org_1_instance_3]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets,
            max_level=1  # Only allow 1 hop
        )
        # Should not find path with max_level=1 (needs 2 hops)
        self.assertNotIn(self.org_1_instance_3.id, result)

    def test_get_instances_paths_with_relation_filter(self):
        """Test that relation filter restricts first edge only."""
        # slot_1 uses predicate_1 which uses relation_1
        # instance_1 -> instance_2 via relation_1
        paths = KnowledgeBaseUtils.get_instances_paths(
            start_instance=self.org_1_instance_1,
            end_instance=self.org_1_instance_2,
            relation_ids={self.org_1_relation_1.id}
        )
        self.assertFalse(paths.empty())
        best_path = paths.get()
        self.assertEqual(best_path[0], 1)  # Direct connection via relation_1

    def test_get_instances_paths_with_non_matching_relation(self):
        """Test that non-matching relation filter returns no paths."""
        # instance_1 -> instance_2 uses relation_1, but we filter for relation_3
        paths = KnowledgeBaseUtils.get_instances_paths(
            start_instance=self.org_1_instance_1,
            end_instance=self.org_1_instance_2,
            relation_ids={self.org_1_relation_3.id}
        )
        self.assertTrue(paths.empty())

    def test_get_instances_paths_first_edge_filter_only(self):
        """Test that relation filter only applies to the first edge, not all edges.

        This tests the key business requirement:
        - User asks "What does X [relation] to, and how does that connect?"
        - First edge must match the relation, but subsequent edges can use any relation.

        Path: instance_1 -> instance_2 (via relation_1) -> instance_3 (via relation_2)
        Filter: relation_1
        Expected: Path found (first edge uses relation_1, second edge uses relation_2 which is OK)
        """
        # Verify the path exists: instance_1 -> instance_2 -> instance_3
        paths_no_filter = KnowledgeBaseUtils.get_instances_paths(
            start_instance=self.org_1_instance_1,
            end_instance=self.org_1_instance_3,
            relation_ids=None
        )
        self.assertFalse(paths_no_filter.empty())
        self.assertEqual(paths_no_filter.get()[0], 2)  # 2 hops

        # With relation_1 filter: should still find path (first edge matches)
        paths_filtered = KnowledgeBaseUtils.get_instances_paths(
            start_instance=self.org_1_instance_1,
            end_instance=self.org_1_instance_3,
            relation_ids={self.org_1_relation_1.id}
        )
        self.assertFalse(paths_filtered.empty())
        best_path = paths_filtered.get()
        self.assertEqual(best_path[0], 2)  # 2 hops
        # Verify first edge uses relation_1
        self.assertEqual(best_path[1][0].predicate.relation_id, self.org_1_relation_1.id)
        # Second edge can use any relation (relation_2 in this case)
        self.assertEqual(best_path[1][1].predicate.relation_id, self.org_1_relation_2.id)

    def test_get_instances_paths_no_filter_regression(self):
        """Regression: None relation_ids should find all paths as before."""
        paths = KnowledgeBaseUtils.get_instances_paths(
            start_instance=self.org_1_instance_1,
            end_instance=self.org_1_instance_2,
            relation_ids=None
        )
        self.assertFalse(paths.empty())

    def test_get_instances_paths_to_multiple_with_relation_filter(self):
        """Test multi-target BFS with relation filter."""
        # instance_1 connects to:
        # - instance_2 via relation_1 (slot_1)
        # - instance_4 via relation_3 (slot_3)
        # - instance_0 via relation_2 (slot_4)
        targets = [self.org_1_instance_2, self.org_1_instance_4, self.org_1_instance_0]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets,
            relation_ids={self.org_1_relation_1.id}
        )
        # Should only find instance_2 (via relation_1), not instance_4 or instance_0
        self.assertIn(self.org_1_instance_2.id, result)
        self.assertNotIn(self.org_1_instance_4.id, result)
        self.assertNotIn(self.org_1_instance_0.id, result)

    def test_get_instances_paths_to_multiple_with_multiple_relations(self):
        """Test multi-target BFS with multiple relations in filter."""
        targets = [self.org_1_instance_2, self.org_1_instance_4, self.org_1_instance_0]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets,
            relation_ids={self.org_1_relation_1.id, self.org_1_relation_3.id}
        )
        # Should find instance_2 (relation_1) and instance_4 (relation_3), but not instance_0 (relation_2)
        self.assertIn(self.org_1_instance_2.id, result)
        self.assertIn(self.org_1_instance_4.id, result)
        self.assertNotIn(self.org_1_instance_0.id, result)

    def test_get_instances_paths_to_multiple_no_filter_regression(self):
        """Regression: None relation_ids should find all paths as before."""
        targets = [self.org_1_instance_2, self.org_1_instance_4, self.org_1_instance_0]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets,
            relation_ids=None
        )
        # Should find paths to all connected targets
        self.assertIn(self.org_1_instance_2.id, result)
        self.assertIn(self.org_1_instance_4.id, result)
        self.assertIn(self.org_1_instance_0.id, result)

    def test_get_instances_paths_to_multiple_first_edge_filter_only(self):
        """Test that relation filter only applies to the first edge in multi-target BFS.

        Path to instance_3: instance_1 -> instance_2 (via relation_1) -> instance_3 (via relation_2)
        Filter: relation_1
        Expected: Should find instance_3 because first edge uses relation_1
        """
        targets = [self.org_1_instance_2, self.org_1_instance_3]
        result = KnowledgeBaseUtils.get_instances_paths_to_multiple(
            start_instance=self.org_1_instance_1,
            end_instances=targets,
            relation_ids={self.org_1_relation_1.id}
        )
        # instance_2: direct connection via relation_1 - should be found
        self.assertIn(self.org_1_instance_2.id, result)
        self.assertEqual(len(result[self.org_1_instance_2.id]), 1)

        # instance_3: 2 hops, first edge via relation_1 - should be found
        self.assertIn(self.org_1_instance_3.id, result)
        self.assertEqual(len(result[self.org_1_instance_3.id]), 2)
        # Verify first edge uses relation_1
        self.assertEqual(
            result[self.org_1_instance_3.id][0].predicate.relation_id,
            self.org_1_relation_1.id
        )

    def test_get_related_instances(self):
        results = KnowledgeBaseUtils.get_related_instances(root_instance=self.org_1_instance_1, predicate_ids=None, level=2)
        self.assertEqual(len(results), 2, results)
        self.assertEqual(len(results[0]), 3, results)

        KnowledgeBaseUtils.get_related_instances(root_instance=self.org_1_instance_1, predicate_ids=None, level=10)
        self.assertEqual(len(results[0]), 3, results)

        predicate_ids = []
        KnowledgeBaseUtils.get_related_instances(root_instance=self.org_1_instance_1, predicate_ids=predicate_ids, level=10)
        self.assertEqual(len(results[0]), 3, results)


    def test_ontology_from_dict(self, model, data=None):
        pass
 
    def test_ontology_to_dict(self, model):
        pass

    def test_instances_from_dict(self, model, data=None):
        pass

    def test_instances_to_dict(self, model):
        pass

    def test_get_url(self, object_type, id):
        pass

