class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow = 0

        for fast in range(len(nums) - 1):
            if nums[fast] != nums[fast + 1]:
                nums[slow] = nums[fast]
                slow += 1
        nums[slow] = nums[-1]
        return slow + 1
if __name__ == '__main__':
    nums = [1,1,2]
    solution = Solution()
    result = solution.removeDuplicates(nums)