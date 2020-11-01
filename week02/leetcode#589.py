class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                s.append(child)
        return res