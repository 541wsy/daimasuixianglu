# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # 栈
        # 压入中，中出栈，加入result，再压入右左，只要栈不空，就pop节点，加入node的右左（条件是右左要非空）

        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            # 加入右左孩子
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

        # #递归
        # result = []

        # def traversal(node):
        #     if not node:
        #         return

        #     result.append(node.val)
        #     traversal(node.left)
        #     traversal(node.right)
        # traversal(root)
        # return result