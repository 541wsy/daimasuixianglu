# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # 前序
        ##单层：合并root1，root2，得到新的点，返回合并后的根节点
        ##递归：递归合并root1.left，root2.left，返回的根节点leftnode,root.left = left.node；right同样处理
        ##终止：root1,root2同时为空；其中一个为空
        if not root1 and not root2:
            return
            # 只要其中一个为空，那么没有继续遍历的必要，合并后就是非空的那个节点为根节点的子树
        elif not root1 and root2:
            return root2
        elif root1 and not root2:
            return root1
        else:
            # root1,root2都非空情形
            root = TreeNode(root1.val + root2.val)

            leftnode = self.mergeTrees(root1.left, root2.left)
            root.left = leftnode

            rightnode = self.mergeTrees(root1.right, root2.right)
            root.right = rightnode

        return root
