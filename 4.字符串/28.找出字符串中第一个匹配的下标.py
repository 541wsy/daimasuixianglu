class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        def get_next(needle):
            # 初始化next数组

            next_ = [0] * len(needle)
            next_[0] = 0
            # 初始化指针：j前缀末尾；i:后缀末尾
            j = 0
            for i in range(1, len(needle)):
                # 如果匹配
                if needle[i] == needle[j]:
                    j += 1

                # 如果不匹配，j往回找可能匹配的更短的位置，最多会往回找两次，两次循环则j=0
                else:
                    while j > 0 and needle[i] != needle[j]:
                        j = next_[j - 1]
                    # 跳出循环，要么循环一次，找到可匹配的前后缀，则长度为j + 1
                    # 要么没找到，则j=0
                    if needle[j] == needle[i]:
                        j += 1
                next_[i] = j
            return next_

        # 计算next数组
        next_ = get_next(needle)
        # 初始化指针
        # i指向文本串，j指向模式串
        j = 0
        i = 0
        while i < len(haystack):

            # 如果匹配
            if needle[j] == haystack[i]:
                j += 1
            # 如果不匹配
            else:
                while j > 0 and needle[j] != haystack[i]:
                    j = next_[j - 1]
                # 循环跳出时，出现两种情况：
                # 1.j>0 找到needle[j] == haystack[i],j+=1
                # 2.j=0,如果此时相等j+=1，如果不等j不动
                if needle[j] == haystack[i]:
                    j += 1

            # j指针左侧的字符一定是匹配的，所以当j跳出，一定全部匹配
            if j == len(needle):
                return i + 1 - j

            i += 1
        return -1


needle = "ababcaabc"
haystack = "ababcaababcaabc"
solution = Solution()
result = solution.strStr(haystack,needle)















