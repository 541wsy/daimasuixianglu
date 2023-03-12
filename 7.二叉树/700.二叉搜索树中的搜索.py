# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # #前序
        # if not root:
        #     return

        # if root.val == val:
        #     node = root
        # elif root.val > val:
        #     node = self.searchBST(root.left, val)
        # elif root.val < val:
        #     node = self.searchBST(root.right, val)

        # return node

        # 迭代
        from collections import deque
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.val == val:
                return node
            elif node.val > val and node.left:
                q.append(node.left)
            elif node.val < val and node.right:
                q.append(node.right)
        return None



