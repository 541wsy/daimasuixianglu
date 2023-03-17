class Solution:
    def partition(self, s):
        path = []
        result = []

        def backtracking(startindex, s):

            #当切到最后一个元素
            if startindex == len(s):
                #此处path不需要判断非空，因为path.append是在回文串时才会加入，一定非空
                result.append(path[:])
                return

            for i in range(startindex, len(s)):
                #切割的子串
                cut_s = s[startindex:i + 1]
                #如果当前切割子串是回文的，加入path
                if cut_s == cut_s[::-1]:
                    path.append(cut_s)
                    #递归
                    backtracking(i + 1, s)
                    #回溯
                    path.pop()

        backtracking(0, s)
        return result

s = 'aab'
solution = Solution()
result = solution.partition(s)