class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(startindex, used, nums):
            # 每层递归都收获元素
            # 当path长度大于等于2，放入结果集
            if len(path) >= 2:
                result.append(path[:])

            # 终止条件
            if startindex == len(nums):
                return
            # 在当前数层定义一个set，记录取过的元素
            set_ = set()
            for i in range(startindex, len(nums)):
                # 递增
                if path and nums[i] < path[-1]:
                    continue
                # 去重
                if nums[i] in set_:
                    continue

                else:
                    set_.add(nums[i])  # 记录取过的元素
                    path.append(nums[i])
                    used[i] = 1

                    # 递归
                    backtracking(i + 1, used, nums)
                    # 回溯
                    path.pop()
                    used[i] = 0

        backtracking(0, [0] * len(nums), nums)
        return result

