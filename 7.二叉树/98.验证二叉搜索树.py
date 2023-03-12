# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right/
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # 判断中序遍历是否有序, 双指针
        pre = None

        def traversal(node):
            nonlocal pre
            if not node:
                return True
            # 左中右
            isleftBST = traversal(node.left)
            if pre and pre.val >= node.val:
                return False
            pre = node  # 更新指针
            isrightBST = traversal(node.right)
            return isleftBST and isrightBST

        return traversal(root)





