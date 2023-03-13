# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        # 与删除二叉搜索树不同在于：这个删除的元素会有多个，所以不能只要找到马上return，有可能还有别的待删除的node
        # 返回：以root为根节点的修建后子树根节点
        if not root:
            return None

        if root.val < low:  # 右子树仍有可能落在区间
            return self.trimBST(root.right, low, high)
        elif root.val > high:  # 左子树仍有可能落在区间
            return self.trimBST(root.left, low, high)

        leftroot = self.trimBST(root.left, low, high)
        rightroot = self.trimBST(root.right, low, high)

        root.left = leftroot
        root.right = rightroot

        return root



