class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []

        def backtracking(startindex, s):
            #终止条件：
            ##path长度等于4并且切割到最后一个
            if len(path) == 4:
                if startindex == len(s):
                    result.append('.'.join(path[:]))
                return

            for i in range(startindex, len(s)):
                cut_s = s[startindex:i+1]
                #continue的情形
                ##1.len(cut_s) > 1 and cut_s[0] == 0
                ##2.int(cut_s) > 255
                if len(cut_s) > 1 and cut_s[0] == '0': #注意这里要用字符的0
                    continue
                elif int(''.join(cut_s)) > 255:
                    continue
                else:
                    path.append(cut_s)
                    backtracking(i+1, s)
                    #回溯
                    path.pop()
        backtracking(0, s)
        return result