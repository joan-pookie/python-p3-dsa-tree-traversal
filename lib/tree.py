class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        """Return the node with the given id using depth-first traversal."""
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            # Take the first node
            node = nodes_to_visit.pop(0)
            
            # Check if this node's id matches
            if node.get('id') == target_id:
                return node
            
            # Add children to the BEGINNING of nodes_to_visit (depth-first)
            nodes_to_visit = node.get('children', []) + nodes_to_visit

        # Return None if not found
        return None
