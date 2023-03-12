# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 和中序后序构造二叉树是类似的思路
        # 后序遍历
        ##参数：数组；返回值：根节点
        ##终止条件：nums为空，返回空
        ##单层：1.找最大值的index；2.切割nums为左右子树leftnums=nums[:index],rightnums=nums[index+1:]；3.递归左右，找到左右子树的根节点；4.连接根节点

        if not nums:
            return

        index = nums.index(max(nums))
        root = TreeNode(nums[index])

        leftnums = nums[:index]
        rightnums = nums[index + 1:]

        leftroot = self.constructMaximumBinaryTree(leftnums)
        rightroot = self.constructMaximumBinaryTree(rightnums)

        root.left = leftroot
        root.right = rightroot

        return root