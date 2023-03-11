"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None
        from collections import deque
        q = deque()
        q.append(root)

        # 每一层遍历，先处理第一个节点，初始化pre=第一个节点
        # 对于后面的节点：pre.next = cur
        # 遍历到最后一个节点，cur.next = None
        while q:
            lenq = len(q)
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if i == lenq - 1:
                    break
                cur.next = q[0]

        return root




