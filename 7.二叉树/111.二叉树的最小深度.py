# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # #后序：
        # ##终止条件：遍历到叶子节点，return 1;求根节点的高度

        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # #递归左右
        # left_h = float('inf')
        # right_h = float('inf')
        # #由于终止条件要求遍历到叶子节点，return，所以在递归左右时，如果根节点空了，就不用递归
        # if root.left:
        #     left_h = self.minDepth(root.left)
        # if root.right:
        #     right_h = self.minDepth(root.right)
        # return 1 + min(left_h, right_h)

        # #后序版本2：考虑三种左右孩子情形
        # if not root:
        #     return 0
        # #递归左右
        # left_h = self.minDepth(root.left)
        # right_h = self.minDepth(root.right)

        # #判断三种情形
        # if not root.left and root.right:
        #     return 1 + right_h
        # elif root.left and not root.right:
        #     return 1 + left_h
        # else:
        #     return 1 + min(left_h, right_h)

        # 层序
        if not root:
            return 0
        from collections import deque
        q = deque()
        q.append(root)

        depth = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                # 只要node在叶子节点，break...
                if not node.left and not node.right:
                    return depth

                # 加入左右孩子
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 更新深度
            depth += 1






