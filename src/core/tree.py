from __future__ import annotations
from typing import Iterator, Optional
import src.helpers.tree_to_ascii as ascii_helper
from collections import deque
import math

class TreeNode:
    DEFAULT_NAME = ''
    DEFAULT_DISTANCE = 1.0

    def __init__(self, /, name: str = DEFAULT_NAME, distance: float = DEFAULT_DISTANCE, children: list[TreeNode] = []):
        self.name = name
        self._children = []
        self.parent = None
        self.children = children
        self.distance = distance
        
    ###################
    # Data properties #
    ###################   
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        assert isinstance(value, str), f"The name of a TreeNode must be a string. Name provided: {value}"
        self._name = value

    @property
    def children(self) -> list[TreeNode]:
        return self._children

    @children.setter
    def children(self, value: list[TreeNode]):
        for child in value:
            self.add_child(child)

    @property
    def parent(self) -> TreeNode:
        return self._parent

    @parent.setter
    def parent(self, value: TreeNode):
        assert isinstance(value, TreeNode) or value is None, "The parent of a TreeNode must be a TreeNode or None"
        self._parent = value
    
    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, value: float):
        assert isinstance(value, float), "The distance value of a TreeNode must be a float."
        self._distance = value

    ######################
    # Computed variables #
    ######################
    @property
    def is_leaf(self) -> bool:
        return not bool(self.children)

    @property
    def is_root(self) -> bool:
        return self.parent == None

    @property  
    def root(self) -> TreeNode:
        if self.parent == None:
            return self
        return self.ancestors[-1]
    
    @property
    def leaves(self) -> list[TreeNode]:
        return list(self.iterate_leaves())

    @property
    def ancestors(self) -> list[TreeNode]:
        return list(self.iterate_ancestors())

    @property
    def descendants(self) -> list[TreeNode]:
        return sum([list(child._iterate_levelorder()) for child in self.children], [])

    @property
    def size(self) -> list[TreeNode]:
        return len(self.descendants) + 1

    ##################
    # Public methods #
    ##################
    def add_child(self, child: TreeNode):
        assert isinstance(child, TreeNode), "Child must be a TreeNode."
        child.parent = self
        self._children.append(child)

    def remove_child(self, child: TreeNode):
        try:
            self._children.remove(child)
        except ValueError as e:
            raise "not yet implemented"
        else:
            child.parent = None

    def iterate_ancestors(self) -> Iterator[TreeNode]:
        current_node = self
        while current_node.parent != None:
            current_node = current_node.parent
            yield current_node 
    
    def iterate_leaves(self) -> Iterator[TreeNode]:
        for node in self._iterate_levelorder():
            if node.is_leaf:
                yield node
    
    def get_distance(self, destination: TreeNode, topology_only = False) -> float:
        """
        Get the distance between two nodes in the tree.
        Normally returns the sum of the weighted distances between the node. If
        the `topology_only` parameter is set, each vertex will have weight 1.0.
        If the nodes belong to different trees, return `math.inf`. 

            Parameters:
                destination: TreeNode
                topology_only: bool
            
            Returns:
                distance: float
        """
        if self == destination:
            return 0.0

        self_ancestors = set(self.ancestors).union([self])
        destination_ancestors = set(destination.ancestors).union([destination])
        different_ancestors = self_ancestors.symmetric_difference(destination_ancestors)

        if not different_ancestors:
            return math.inf

        return len(different_ancestors) + 2 if topology_only else sum([node.distance for node in different_ancestors])

    def get_common_ancestor(self, other: TreeNode) -> Optional[TreeNode]:
        ancestors = self.ancestors

        for other_ancestor in other.ancestors:
            if other_ancestor in ancestors:
                return other_ancestor

        return None

    def get_all_distances(self) -> DistanceMatrix:
        raise "Not yet implemented"

    def to_newick(self) -> str:
        newick = ""
        if not self.is_leaf:
            newick += "("
        newick +=  ",".join(map(lambda x: x.to_newick(), self.children))
        if not self.is_leaf:
            newick += ")"
        newick += self.name + ("" if self.distance == self.DEFAULT_DISTANCE else f":{self.distance:.6f}")
        return newick

    ######################
    # Built-in functions #
    ######################
    def __str__(self) -> str:
        return ascii_helper.tree_to_ascii(self)
    
    def __repr__(self) -> str:
        return f'TreeNode(name="{self.name}", distance={self.distance}, children=[{", ".join([child.__repr__() for child in self.children])}])'

    def __len__(self) -> int:
        return len(self.leaves)
    
    def __iter__(self) -> Iterator[TreeNode]:
        return self.iterate_leaves()
    
    def __list__(self) -> list[TreeNode]:
        return list(self.iterate_leaves())

    ###################
    # Private methods #
    ###################
    def _iterate_levelorder(self) -> Iterator[TreeNode]:
        descendants: deque[TreeNode] = deque([self])
        while descendants:
            yield descendants[0]
            descendants.extend(descendants.popleft().children)