# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序，双指针
        pre = None
        mindiff = float('inf')  # 直接操作全局变量，不需要return

        def traversal(node):
            nonlocal pre
            nonlocal mindiff

            if not node:
                return
            traversal(node.left)
            if pre:
                mindiff = min(abs(node.val - pre.val), mindiff)
            # 移动指针
            pre = node
            traversal(node.right)

        traversal(root)
        return mindiff

