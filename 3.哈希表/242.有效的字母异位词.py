class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        abc = [0] * 26  # 开一个26个字母长度的哈希表（即数组）
        ## 小写字母的ASCII码是连续的，使用ord('a')可以得到字符'a'的ASCII码

        ## abc的每个位置存放该位置字母的出现次数

        for x in s:
            abc[ord(x) - ord('a')] += 1

        for x in t:
            abc[ord(x) - ord('a')] -= 1

        # 判断数组abc是否所有元素都为0
        for x in abc:
            if x != 0:
                return False

        return True

