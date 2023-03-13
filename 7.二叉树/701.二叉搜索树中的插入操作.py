# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # 迭代法
        if not root:
            return TreeNode(val)

        from collections import deque
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.val > val and node.left:
                    q.append(node.left)
                elif node.val > val and not node.left:
                    node.left = TreeNode(val)
                elif node.val < val and node.right:
                    q.append(node.right)
                elif node.val < val and not node.right:
                    node.right = TreeNode(val)
        return root

        # #递归：后序
        # if not root:
        #     return TreeNode(val)

        # if root.val < val: #往右搜索
        #     rightnode = self.insertIntoBST(root.right, val)
        #     root.right = rightnode
        # else:
        #     leftnode = self.insertIntoBST(root.left, val)
        #     root.left = leftnode

        # return root


