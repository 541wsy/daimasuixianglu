class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for a in range(len(nums) - 3):
            # 对a去重
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            ##下面进行三数之和
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                left = b + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        # 对left，right去重
                        while left != right and nums[left] == nums[left + 1]: left += 1
                        while left != right and nums[right] == nums[right - 1]: right -= 1
                        result.append([nums[a], nums[b], nums[left], nums[right]])
                        left += 1
                        right -= 1
        return result

