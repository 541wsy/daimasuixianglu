# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 前序
        ##返回：以nums构造的平衡BST根节点
        ##单层：1.nums二分；2.创造根节点；3.递归左右；4.连接左右
        if not nums:
            return

        index = len(nums) // 2
        leftnums = nums[:index]
        rightnums = nums[index + 1:]

        root = TreeNode(nums[index])

        leftroot = self.sortedArrayToBST(leftnums)
        rightroot = self.sortedArrayToBST(rightnums)

        root.left = leftroot
        root.right = rightroot

        return root