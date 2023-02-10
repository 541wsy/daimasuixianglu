class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 遍历nums的每个元素，计算target-num = x,如果x之前遍历过，则返回x的下标和当前下标
        # 使用一个字典存放遍历过程，key是遍历元素，value是下标
        record = {}
        for ind, num in enumerate(nums):
            x = target - num
            if x in record.keys():
                return [ind, record[x]]
            record[num] = ind
