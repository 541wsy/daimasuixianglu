# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            # 返回值：以node为根节点树的高度，-1表示不平衡
            if not node:
                return 0
            left_h = get_height(node.left)
            right_h = get_height(node.right)

            maxh = max(left_h, right_h)
            minh = min(left_h, right_h)

            if minh == -1 or maxh - minh > 1:
                return -1
            else:
                return 1 + max(left_h, right_h)

        # 调用get_height(root)的返回值表明的root节点的平衡状态，递归是在get_height中完成的
        if get_height(root) == -1:
            return False
        else:
            return True

