from treenode import TreeNode
import numpy as np
from typing import Union

class DistanceMatrix:
    def __init__(self, _tree: TreeNode):
        self._tree = _tree

        nodes = list(self._tree._iterate_levelorder())
        self._init_matrix(len(nodes))
        self._init_node_index_dict(nodes)
        self._init_distances()

    def _init_matrix(self, size):    
        self._matrix = np.zeros(shape=(size, size), dtype=np.float64)

    def _init_node_index_dict(self, nodes):
        self._node_index_dict = {nodes[i]: i for i in range(0,len(nodes))}
        self._index_node_dict = nodes

    def _init_distances(self):
        # We iterate through the levels of the _tree. Every level we know that we have all the distances between the nodes on the level above so we only have to do
        # leaf1.dist + leaf2.dist + distance_matrix.distance_between(leaf1.up, leaf2.up)
        size = len(self._matrix)
        for i in range(1, size):
            node = self._index_node_dict[i]
            distance = node.distance
            parent = self._node_index_dict[node.parent]
            
            self._matrix[i, 0:i] = self._matrix[parent, 0:i] + distance
            self._matrix[0:i, i] = self._matrix[i, 0:i]

    def get_distance(self, leaf1: TreeNode, leaf2: TreeNode) -> float:
        """
        Get distance between leaf1, leaf2 using subscript notation
        I.e., distance_matrix[leaf1, leaf2]
        """
        return self._matrix[self._node_index_dict[leaf1], self._node_index_dict[leaf2]] 

    def _set_distance(self, leaf1: TreeNode, leaf2: TreeNode, distance: float):
        """
        Set distance between leaf1, leaf2 using subscript notation
        I.e., distance_matrix[leaf1, leaf2] = distance
        """
        leaf1_index = self._node_index_dict[leaf1]
        leaf2_index = self._node_index_dict[leaf2]

        self._matrix[leaf1_index, leaf2_index] = distance
        self._matrix[leaf2_index, leaf1_index] = distance

    def _get_distances(self, leaves1: Union[TreeNode, list[TreeNode]], leaves2: Union[TreeNode, list[TreeNode]]) -> np.ndarray:
        if not isinstance(leaves1, list):
            leaves1 = [leaves1]
        if not isinstance(leaves2, list):
            leaves2 = [leaves2]

        leaves1_indices = [self._node_index_dict[leaf] for leaf in leaves1]
        leaves2_indices = [self._node_index_dict[leaf] for leaf in leaves2]

        leaves1_mesh, leaves2_mesh = np.meshgrid(leaves1_indices, leaves2_indices)

        # The matrix is symmetrical, it's enough to only look at coordinates with x < y. 
        # This also excludes comparing a leaf with itself. To include this option, set < to <=
        valid_indices = leaves1_mesh != leaves2_mesh

        return self._matrix[leaves1_mesh[valid_indices], leaves2_mesh[valid_indices]]

    def get_min_distance(self, leaves1: Union[TreeNode, list[TreeNode]], leaves2: Union[TreeNode, list[TreeNode]]) -> float:
        return np.min(self._get_distances(leaves1, leaves2))

    def get_median_distance(self, leaves1: Union[TreeNode, list[TreeNode]], leaves2: Union[TreeNode, list[TreeNode]]) -> float:
        return np.median(self._get_distances(leaves1, leaves2))

    def __str__(self):
        return str(self._matrix)

    def __repr__(self):
        return f'DistanceMatrix({repr(self._tree)})'