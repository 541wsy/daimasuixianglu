class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        # 翻转前k个次数
        n = len(s) // (2 * k)

        for i in range(n):
            left = i * 2 * k
            right = left + k - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        # 计算剩余长度
        m = len(s) % (2 * k)
        left = len(s) - m
        if m < k:
            right = len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        else:
            right = left + k - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)





