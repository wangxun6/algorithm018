class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        cur = TreeNode(preorder[0])
        index = inorder.index(cur.val)
        cur.left = self.buildTree(preorder[1 : index + 1],inorder[:index])
        cur.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return cur