class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(used, nums):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # 如果路径中有nums[i],跳过
                if used[i]:
                    continue
                else:
                    path.append(nums[i])
                    used[i] = 1
                    # 递归
                    backtracking(used, nums)
                    # 回溯
                    path.pop()
                    used[i] = 0

        backtracking([0] * len(nums), nums)
        return result


