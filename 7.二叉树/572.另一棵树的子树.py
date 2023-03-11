# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # 前序遍历，只要遍历到subroot.val，开始遍历两棵树（后序递归compare函数）
        def compare(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False

            elif root1.val != root2.val:
                return False
            else:
                # 判断左孩子是否相等
                issameleft = compare(root1.left, root2.left)
                # 判断右孩子是否相等
                issameright = compare(root1.right, root2.right)
                return issameleft and issameright

        # 开始前序遍历，找subroot.val
        ##终止条件root为空;root找到subroot子树
        if not root:
            return False
        if root.val == subRoot.val:
            ##继续判断子树是否相等
            issame = compare(root, subRoot)
            if issame:
                return True
        ##如果没找到，继续向左右递归

        findleft = self.isSubtree(root.left, subRoot)
        findright = self.isSubtree(root.right, subRoot)
        return findleft or findright



