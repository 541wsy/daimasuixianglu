class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0

        result = 0
        curcover = 0
        nextcover = 0

        for i in range(len(nums) - 1):
            # 计算nextcover:如果curcover走不到，下一次的最大cover
            nextcover = max(nextcover, i + nums[i])
            # 如果走到curcover的最后一个还没到，result += 1，更新curcover为nextcover
            # 此处体现了贪心的策略，在curcover的范围内跳的终点是那个cover最大的点
            if i == curcover:
                # 如果当前没走到，就需要考虑下一跳
                if curcover < len(nums) - 1:
                    result += 1
                    curcover = nextcover
                    # 如果下一跳能到终点，return
                    if nextcover >= len(nums) - 1:
                        return result


nums = [1,2]
solution = Solution()
result = solution.jump(nums)