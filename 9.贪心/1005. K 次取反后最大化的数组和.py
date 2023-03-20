class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        # 优先满足绝对值大的数
        ##按照绝对值大小进行排序，遇到负数取反，遇到正数跳过不处理
        ##如果最后k还有剩余，剩下只有正数，对最小正数操作，即使取成负数，也是对总和影响最小的方案
        nums = sorted(nums, key=abs, reverse=True)  # 降序
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k > 0:
            nums[-1] *= ((-1) ** k)

        return sum(nums)

nums = [-8,3,-5,-3,-5,-2]
k = 6
solution = Solution()
result = solution.largestSumAfterKNegations(nums, k)


