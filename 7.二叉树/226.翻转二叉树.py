# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 前序
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # #后序
        # if not root:
        #     return

        # leftnode = self.invertTree(root.left)
        # rightnode = self.invertTree(root.right)

        # root.left = rightnode
        # root.right = leftnode
        # return root

        # #迭代
        # #层序遍历，先放右孩子
        # if not root:
        #     return None
        # from collections import deque
        # q = deque()
        # q.append(root)

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #         #交换node的左右孩子
        #         node.left, node.right= node.right, node.left

        # return root