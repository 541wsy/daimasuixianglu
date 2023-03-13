# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 右中左遍历
        ##定义全局变量count_ 进行累加
        ##不需要返回值，直接操控全局变量，和节点的val
        count_ = 0

        def traversal(node):
            nonlocal count_
            if not node:
                return
            traversal(node.right)

            count_ += node.val
            node.val = count_

            traversal(node.left)

        traversal(root)
        return root
