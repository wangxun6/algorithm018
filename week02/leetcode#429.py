"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        out = []
        while queue:
            child = []
            node = []
            for item in queue:
                child.append(item.val)
                if item.children: node += item.children
            out.append(child)
            queue = node
        return out