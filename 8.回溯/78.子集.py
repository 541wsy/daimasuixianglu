class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        path = []

        def backtracking(startindex, nums):
            if startindex == len(nums):
                return

            for i in range(startindex, len(nums)):
                path.append(nums[i])
                result.append(path[:])  # 在每个节点收获结果

                # 进入下一层递归
                backtracking(i + 1, nums)
                # 回溯
                path.pop()

        backtracking(0, nums)
        return result