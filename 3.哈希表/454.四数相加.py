from collections import defaultdict
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        result = 0
        for i in nums1:
            for j in nums2:
                sum12 = i + j
                dic[sum12] += 1
        for i in nums3:
            for j in nums4:
                sum34 = i + j
                x = 0 - sum34
                if x in dic.keys():
                    result += dic[x]
        return result