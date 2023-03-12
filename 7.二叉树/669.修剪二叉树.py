# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root, low, high):
        #后序
        if not root:
            return
        #如果找到需要删除的节点
        if root.val < low or root.val > high:
            #1.左右空，返回None
            #2.左右其中一个非空，返回非空节点
            #3.左右都非空，返回右节点
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        leftnode = self.trimBST(root.left, low,high)
        rightnode = self.trimBST(root.right, low,high)

        root.left = leftnode
        root.right = rightnode

        return root
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(2)

node1.left = node2
node1.right = node3
node2.left = None
node2.right = node4
node3.left = None
node3.right = None

solution = Solution()
result = solution.trimBST(node1,low=1,high=2)
