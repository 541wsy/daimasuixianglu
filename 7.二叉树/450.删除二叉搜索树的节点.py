# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # 后序
        ##终止条件：没找到，return；找到了：1.叶子节点；2.非叶子：右子树即位，左孩子放到右子树的最左的左孩子
        if not root:
            return

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                ##找右子树的最左节点
                cur = root.right
                while cur.left:
                    cur = cur.left
                ##root.left放在cur的左子树
                cur.left = root.left
                return root.right
        leftroot = self.deleteNode(root.left, key)
        rightroot = self.deleteNode(root.right, key)

        root.left = leftroot
        root.right = rightroot

        return root