# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 层序遍历，输出每一层的最右元素
        if not root:
            return []
        from collections import deque

        q = deque()
        q.append(root)
        result = []
        while q:
            q_len = len(q)  # 注意这里要先记录当前遍历的长度，否则判断i==len(q) - 1时，q的长度 是不断变化的，但是for里面可以用len(q)
            for i in range(len(q)):
                node = q.popleft()

                if i == q_len - 1:
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result



