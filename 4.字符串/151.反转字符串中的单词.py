class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 全部翻转字符
        s = list(s)[::-1]
        # 删除多余空格
        ##符合要求的单词特点：
        # 1.s[fast]!=" " and slow == 0
        # 2.s[fast] != " " 继续判断，如果fast-1是空格，则赋值两次，如果不是空格，赋值一次

        fast, slow = 0, 0
        while fast <= len(s) - 1:
            if s[fast] != " " and slow == 0:
                s[slow] = s[fast]
                slow += 1
            elif s[fast] != " " and s[fast - 1] == " ":
                s[slow] = " "
                slow += 1
                s[slow] = s[fast]
                slow += 1
            elif s[fast] != " " and s[fast - 1] != " " and fast > 0:
                s[slow] = s[fast]
                slow += 1
            fast += 1
        result1 = s[:slow]
        # 反转每个单词
        fast, slow = 0, 0
        while fast <= len(result1) - 1:
            if result1[fast] == ' ':
                result1[slow:fast] = result1[slow:fast][::-1]
                slow = fast + 1
            fast += 1
        result1[slow:fast] = result1[slow:fast][::-1]
        return ''.join(result1)
