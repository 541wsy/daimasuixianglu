class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        '''
        方法1：计数
        将两个字符串分别用数组进行计数（26长度的一维数组）
        如果magazine的每一位都大于等于ransmoNote的计数数组，返回True，否则返回False
        '''

        count_rans = [0] * 26
        count_maga = [0] * 26

        for ch in ransomNote:
            count_rans[ord(ch) - ord('a')] += 1
        for ch in magazine:
            count_maga[ord(ch) - ord('a')] += 1

        for rans, maga in zip(count_rans, count_maga):
            if maga < rans:
                return False
        return True