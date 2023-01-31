class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        result = float('inf') #定义一个无穷大
        tmp = 0 #当前区间加和
        for j in range(len(nums)):
            tmp += nums[j] #此处不能用sum
            while tmp >= target:
                result = min(j-i+1, result)
                #移动指针后的tmp
                tmp -= nums[i]
                i +=1
        return 0 if result == float('inf') else result

nums = [1,4,4]
solution = Solution()
result = solution.minSubArrayLen(4,nums)
print(result)