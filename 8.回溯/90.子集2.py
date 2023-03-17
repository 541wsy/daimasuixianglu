class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = [[]]
        nums.sort() #nums需要先sort，才能去重
        def backtracking(starindex, used, nums):
            if starindex == len(nums):
                return

            for i in range(starindex, len(nums)):
                #去重
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                else:
                    path.append(nums[i])
                    result.append(path[:])
                    used[i] = 1
                    #递归
                    backtracking(i+1, used, nums)
                    #回溯
                    path.pop()
                    used[i] = 0
        backtracking(0, [0]*len(nums), nums)
        return result