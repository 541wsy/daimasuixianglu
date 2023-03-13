# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # #普通二叉树做法
        # #后序遍历
        # #找左子树的找到节点，右子树的找到节点，找到空return NOne
        # if not root or root.val == q.val or root.val == p.val:
        #     return root
        # leftnode = self.lowestCommonAncestor(root.left, p, q)
        # rightnode = self.lowestCommonAncestor(root.right, p, q)

        # if leftnode and rightnode:
        #     return root
        # elif not leftnode and rightnode:
        #     return rightnode
        # elif leftnode and not rightnode:
        #     return leftnode
        # else:
        #     return None

        # 二叉搜索树：只要找到节点在p,q区间内，return root
        if not root:
            return
        if root.val > max(p.val, q.val):  # 向左搜索
            node = self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            node = self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        if node:
            return node






