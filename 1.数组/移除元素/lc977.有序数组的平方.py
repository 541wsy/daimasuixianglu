class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        result = nums[:]
        slow = len(result) - 1
        while left <= right:
            if nums[right] >= nums[left]:
                result[slow] = nums[right] ** 2
                right -= 1
            else:
                result[slow] = nums[left] ** 2
                left += 1
            slow += 1
nums = [-4,-1,0,3,10]
solution = Solution()
result = solution.sortedSquares(nums)