# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #后序是中右左的反转
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


        # #递归法
        # result = []
        # def traversal(cur):
        #     if not cur:
        #         return

        #     traversal(cur.left)
        #     traversal(cur.right)
        #     result.append(cur.val)
        # traversal(root)
        # return result
