
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 层序
        depth = 0
        if not root:
            return 0
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

        # #后序递归==找根节点的高度
        # if not root:
        #     return 0
        # left_h = self.maxDepth(root.left)
        # right_h = self.maxDepth(root.right)
        # return 1 + max(left_h, right_h)
