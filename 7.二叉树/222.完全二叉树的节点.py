# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        # 完全二叉树递归解法：递归到一定深度一定存在左子树或者右子树为满二叉树（终止条件）
        # 如何判断满二叉树：从根节点向左右分别计算深度，深度相等则是满二叉树（只适用于完全二叉树）
        ##终止条件：root为空，return 0；root为根节点的树是完全二叉树
        if not root:
            return 0
        cur_left = root.left
        cur_right = root.right

        # 遍历左侧深度
        depth_left = 0
        while cur_left:
            cur_left = cur_left.left
            depth_left += 1
        # 遍历右侧深度
        depth_right = 0
        while cur_right:
            cur_right = cur_right.right
            depth_right += 1
        # 如果左右深度相等，说明为满二叉树
        if depth_left == depth_right:
            return 2 ** (depth_left + 1) - 1

        # 如果不是满二叉树，继续向左右遍历，至少叶子节点也会是满二叉树
        else:
            leftnum = self.countNodes(root.left)
            rightnum = self.countNodes(root.right)
            return 1 + leftnum + rightnum

        # #普通二叉树：层序
        # counts = 0
        # if not root:
        #     return counts
        # from collections import deque
        # q = deque()
        # q.append(root)

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         counts += 1
        #         if node.left:
        #             q.append(node.left)

        #         if node.right:
        #             q.append(node.right)
        # return counts

        # #普通二叉树，后序
        # if not root:
        #     return 0
        # leftnum = self.countNodes(root.left)
        # rightnum = self.countNodes(root.right)
        # #中
        # return 1 + leftnum + rightnum
