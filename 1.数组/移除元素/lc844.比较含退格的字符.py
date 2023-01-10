class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #方法1：双指针
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
        #方法2：栈
        def get_string(s):
            stack = []  # 建立一个空栈
            s = list(s)
            for element in s:
                if element != "#":  # 如果没有碰到退格,进栈
                    stack.append(element)
                else:  # 如果碰到退格
                    if len(stack) == 0:
                        continue
                    else:
                        stack.pop()
            return stack

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