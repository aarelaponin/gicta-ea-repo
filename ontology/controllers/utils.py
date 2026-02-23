from queue import PriorityQueue
from uuid import UUID

from django.db.models import Q

from ontology.models import OConcept, OInstance, OPredicate, ORelation, OSlot

DEFAULT_MAX_LEVEL = 5


class KnowledgeBaseUtils:

    def get_parent_concepts(concept, max_level=DEFAULT_MAX_LEVEL):
        return KnowledgeBaseUtils.get_recursive_parent_concepts(concept, results=[], level=0, max_level=max_level)

    def get_recursive_parent_concepts(concept, results, level, max_level=DEFAULT_MAX_LEVEL):
        if level > max_level:
            return results
        parents = [x.subject for x in OPredicate.objects.filter(object=concept, relation__type=ORelation.INHERITANCE_SUPER_IS_SUBJECT)] + [
            x.object for x in OPredicate.objects.filter(subject=concept, relation__type=ORelation.INHERITANCE_SUPER_IS_OBJECT)]
        for x in parents:
            results = results + KnowledgeBaseUtils.get_recursive_parent_concepts(
                concept=x, results=results, level=level+1, max_level=DEFAULT_MAX_LEVEL)
        return [(x, level) for x in parents] + results

    def get_child_concepts(concept, max_level=DEFAULT_MAX_LEVEL):
        return KnowledgeBaseUtils.get_recursive_child_concepts(concept, results=[], level=0, max_level=max_level)

    def get_recursive_child_concepts(concept, results, level, max_level=DEFAULT_MAX_LEVEL):
        if level > max_level:
            return results
        children = [x.subject for x in OPredicate.objects.filter(object=concept, relation__type=ORelation.INHERITANCE_SUPER_IS_OBJECT)] + [
            x.object for x in OPredicate.objects.filter(subject=concept, relation__type=ORelation.INHERITANCE_SUPER_IS_SUBJECT)]
        for x in children:
            results = results + KnowledgeBaseUtils.get_recursive_child_concepts(
                concept=x, results=results, level=level+1, max_level=DEFAULT_MAX_LEVEL)
        return [(x, level) for x in children] + results

    def get_related_object_concepts(concept, predicate_ids, level=0, max_level=DEFAULT_MAX_LEVEL):
        predicates = OPredicate.objects.filter(subject=concept)
        if predicate_ids is not None and isinstance(predicate_ids, list):
            predicates = predicates.filter(id__in=predicate_ids)

        if level >= max_level:
            return [(x.object, level) for x in predicates]
        results = []
        for x in predicates:
            results = results + KnowledgeBaseUtils.get_related_object_concepts(
                level=level + 1, concept=x.object, predicate_ids=predicate_ids, max_level=max_level)
        return [(x.object, level) for x in predicates] + results

    def get_related_subject_concepts(concept, predicate_ids, level=0, max_level=DEFAULT_MAX_LEVEL):
        predicates = OPredicate.objects.filter(object=concept)
        if predicate_ids is not None and isinstance(predicate_ids, list):
            predicates = predicates.filter(id__in=predicate_ids)

        if level >= max_level:
            return [(x.subject, level) for x in predicates]
        results = []
        for x in predicates:
            results = results + KnowledgeBaseUtils.get_related_subject_concepts(
                level=level + 1, concept=x.subject, predicate_ids=predicate_ids, max_level=max_level)
        return [(x.subject, level) for x in predicates] + results


    def get_instances_paths(start_instance, end_instance, relation_ids=None):
        """Find paths between two instances using BFS for efficiency.

        Args:
            start_instance: The starting OInstance
            end_instance: The target OInstance
            relation_ids: Optional set of relation IDs to filter the FIRST edge only.
                          If provided, only first edges from start_instance using these
                          relations are traversed. Subsequent edges can use any relation.

        Returns:
            PriorityQueue containing (path_length, path) tuples
        """
        q = PriorityQueue(maxsize=5)

        # Load all slots into memory for the same model (much faster than per-query)
        all_slots = list(OSlot.objects.filter(model=start_instance.model).select_related('subject', 'object', 'predicate__relation'))

        # Build FULL adjacency list (no filtering here - filter applied during BFS)
        adjacency = {}
        for slot in all_slots:
            if slot.subject_id:
                if slot.subject_id not in adjacency:
                    adjacency[slot.subject_id] = []
                adjacency[slot.subject_id].append((slot, slot.object_id))
            if slot.object_id:
                if slot.object_id not in adjacency:
                    adjacency[slot.object_id] = []
                adjacency[slot.object_id].append((slot, slot.subject_id))

        # BFS to find paths
        from collections import deque
        queue = deque()
        queue.append((start_instance.id, [], set()))

        while queue:
            current_id, path, visited = queue.popleft()

            if current_id == end_instance.id and path:
                q.put((len(path), path))
                if q.full():
                    break
                continue

            if len(path) >= DEFAULT_MAX_LEVEL:
                continue

            for slot, next_id in adjacency.get(current_id, []):
                if slot.id not in visited and next_id:
                    # Only apply relation filter on FIRST edge (from start instance)
                    if len(path) == 0 and relation_ids:
                        if slot.predicate.relation_id not in relation_ids:
                            continue

                    new_visited = visited.copy()
                    new_visited.add(slot.id)
                    new_path = path + [slot]
                    queue.append((next_id, new_path, new_visited))

        return q

    def get_instances_paths_to_multiple(start_instance, end_instances, max_level=DEFAULT_MAX_LEVEL, relation_ids=None):
        """Find shortest paths to multiple target instances in a single BFS traversal.

        Args:
            start_instance: The starting OInstance
            end_instances: List of target OInstance objects
            max_level: Maximum path depth (default 5)
            relation_ids: Optional set of relation IDs to filter the FIRST edge only.
                          If provided, only first edges from start_instance using these
                          relations are traversed. Subsequent edges can use any relation.

        Returns:
            dict: Mapping of target instance ID -> list of OSlot objects representing the path
        """
        from collections import deque

        target_ids = set(inst.id for inst in end_instances)
        found_paths = {}

        if not target_ids:
            return found_paths

        # Load all slots into memory (same optimization as existing get_instances_paths)
        all_slots = list(OSlot.objects.filter(model=start_instance.model).select_related('subject', 'object', 'predicate'))

        # Build FULL adjacency list (no filtering here - filter applied during BFS)
        adjacency = {}
        for slot in all_slots:
            if slot.subject_id:
                if slot.subject_id not in adjacency:
                    adjacency[slot.subject_id] = []
                adjacency[slot.subject_id].append((slot, slot.object_id))
            if slot.object_id:
                if slot.object_id not in adjacency:
                    adjacency[slot.object_id] = []
                adjacency[slot.object_id].append((slot, slot.subject_id))

        # BFS to find shortest paths to all targets
        queue = deque([(start_instance.id, [], set())])
        visited_nodes = {start_instance.id}

        while queue and len(found_paths) < len(target_ids):
            current_id, path, visited_slots = queue.popleft()

            # Check if we've reached a target (and have a path to it)
            if current_id in target_ids and path:
                if current_id not in found_paths:
                    found_paths[current_id] = path
                # Don't use continue - we still need to explore from this node
                # to find paths to other targets that may be reachable through it

            # Respect max level
            if len(path) >= max_level:
                continue

            # Explore neighbors
            for slot, next_id in adjacency.get(current_id, []):
                if slot.id not in visited_slots and next_id:
                    # Only apply relation filter on FIRST edge (from start instance)
                    if len(path) == 0 and relation_ids:
                        if slot.predicate.relation_id not in relation_ids:
                            continue

                    # Allow visiting nodes if they haven't been visited yet
                    if next_id not in visited_nodes:
                        new_visited = visited_slots.copy()
                        new_visited.add(slot.id)
                        queue.append((next_id, path + [slot], new_visited))
                        visited_nodes.add(next_id)

        return found_paths

    def get_instances_path_recursive(slot, end_instance, path, visited_ids, paths, level=0, max_level=DEFAULT_MAX_LEVEL):
        """Deprecated: Use get_instances_paths with BFS instead."""
        if end_instance == slot.object or end_instance == slot.subject:
            paths.put((len(path), list(path)))
            return None

        if level >= max_level:
            return None

        for x in OSlot.objects.filter((Q(subject=slot.object)|Q(object=slot.subject)|Q(subject=slot.subject)|Q(object=slot.object))):
            if x.id not in visited_ids:
                new_path = list(path)
                new_path.append(x)
                new_visited = visited_ids.copy()
                new_visited.add(x.id)
                KnowledgeBaseUtils.get_instances_path_recursive(slot=x, end_instance=end_instance, path=new_path, visited_ids=new_visited, paths=paths, level=level + 1, max_level=max_level)
        
     
    def get_related_instances(root_instance, predicate_ids, level):
        results = {}
        predicates = OPredicate.objects.filter(model=root_instance.model)
        if predicate_ids and isinstance(predicate_ids, list):
            predicates = predicates.filter(id__in=predicate_ids)
        
        results[0] = [(None, root_instance)]
        already_found = set([root_instance])
        KnowledgeBaseUtils.get_related_instances_recusrsive(results=results, already_found=already_found, instance=root_instance, predicates=predicates, level=1, max_level=level)
        return results

    def get_related_instances_recusrsive(results, already_found, instance, predicates, level, max_level):
        tmp_results = []
        if level >= max_level:
            return tmp_results
        
        for i in results[level-1]:
            tmp_results += [(x, x.object) for x in OSlot.objects.filter(subject=i[1], predicate__in=predicates).all() if x.object not in already_found] + [(x, x.subject) for x in OSlot.objects.filter(object=i[1], predicate__in=predicates).all() if x.subject not in already_found]
        
        already_found.update([x[1] for x in tmp_results])
        results[level] = set(tmp_results)
        KnowledgeBaseUtils.get_related_instances_recusrsive(results=results, already_found=already_found, instance=instance, predicates=predicates, level=level + 1, max_level=max_level)
