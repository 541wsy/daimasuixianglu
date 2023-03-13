# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 后序，传入根节点，返回找到的node
        if not root or root.val == q.val or root.val == p.val:
            return root

        leftnode = self.lowestCommonAncestor(root.left, p, q)
        rightnode = self.lowestCommonAncestor(root.right, p, q)

        if leftnode and rightnode:
            return root
        elif leftnode and not rightnode:
            return leftnode
        elif not leftnode and rightnode:
            return rightnode
        else:
            return None
