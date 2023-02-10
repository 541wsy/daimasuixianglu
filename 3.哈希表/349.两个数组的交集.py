class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # # 方法1：字典做法
        # result = []
        # # nums1转化为hash table(字典)
        # dic1 = {}
        # for num in nums1:
        #     dic1[num] = 1 #此处等于1，使得哈希表dic1去重

        # # 循环nums2的元素，如果在哈希表中，即dic1的keys中，append到结果，同时为了去重，将该key的value置为0
        # for num in nums2:
        #     if num in dic1.keys() and dic1[num] == 1:
        #         result.append(num)
        #         dic1[num] = 0
        # return result

        # 方法2：数组做法
        result = []
        # nums1转化为数组哈希表，由于元素值<=1000，开辟一个1000长度的数组，下标i对应元素若等于1，i在nums中
        hash1 = [0] * 1000
        for num in nums1:
            hash1[num] = 1

        for num in nums2:
            if hash1[num] == 1:
                result.append(num)
                hash1[num] = 0
        return result