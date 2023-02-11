class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        #双指针，对称位置交换
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            #移动指针
            left += 1
            right -= 1
        return s