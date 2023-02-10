class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        nums.sort()
        for i in range(len(nums) - 2):
            # 对第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # 如果找到，进行去重处理
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 添加去重后的结果
                    result.append([nums[i], nums[left], nums[right]])
                    # 移动指针
                    right -= 1
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return result


'''
注：对第2，3个数字去重不能再添加结果之前去重，因为这样对于[-2,0,1,1,2]，这样的数组，会由于对right去重，使得left，right无法取到1，1
'''

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
solution = Solution()
result = solution.threeSum(nums)