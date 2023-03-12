# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 后序
        ##参数：左右子树数组
        ##返回值：返回根节点
        ##单层：创建根节点，
        ##递归：找左子树的中序和后序，找右子树的中序和后序
        if not inorder:
            return
            # 1.后序找到根节点
        # 2.找到根节点在中序的index
        # 3.切割中序,leftin = inorder[:index],rightin=inorder[index+1:]
        # 4.切割后序,leftpost = postorder[:index],rightpost=postorder[index:-1]
        root = TreeNode(postorder[-1])

        for index in range(len(inorder)):
            if inorder[index] == root.val:
                break

        leftin = inorder[:index]
        rightin = inorder[index + 1:]

        leftpost = postorder[:index]
        rightpost = postorder[index:-1]

        leftroot = self.buildTree(leftin, leftpost)
        rightroot = self.buildTree(rightin, rightpost)

        root.left = leftroot
        root.right = rightroot

        return root

