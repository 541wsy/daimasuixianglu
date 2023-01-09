class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def get_string(s):
            slow = -1


            for fast in range(len(s)):

                if s[fast] != '#':
                    if slow < 0:  # 字符串为空
                        continue
                    slow += 1
                    s[slow] = s[fast]

                else:
                    slow -= 1
            return s[:slow + 1]

        s_result = get_string(s)
        t_result = get_string(t)
        if s_result == t_result:
            return True
        else:
            return False
if __name__ == '__main__':
    s = "y#fo##f"
    t = "y#f#o##f"
    solution = Solution()
    result = solution.backspaceCompare(list(s),list(t))