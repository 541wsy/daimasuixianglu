from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 初始化
        i = 0
        needmap = defaultdict(int) #维护当前result和t的差距状态，正数表示：res中差多少，负数表示：res中多了多少
        needcount = len(t) #维护当前差距目标字符个数
        res = '' #初始结果为空字符

        #初始化needmap
        for char in t:
            needmap[char] += 1

        #移动右指针
        for j in range(len(s)):
             #如果当前搜索的右指针在t中
            if s[j] in needmap:
                #如果res中差s[j]，即s[j]在needmap中是正数
                if needmap[s[j]] > 0:
                    needcount -= 1 #差距个数减少
                needmap[s[j]] -= 1 #更改差距状态


            #当满足条件，开始压缩
            while needcount == 0:
                #判断当前结果是否为最小长度，如果当前搜索结果长度更小，则更新结果
                if not res or j - i + 1 < len(res):
                    res = s[i:j+1]

                #移动指针，注意移动指针的过程会改变needmap和needcount的状态
                if s[i] in needmap:
                    if needmap[s[i]] == 0:
                        needcount += 1
                    needmap[s[i]] += 1
                i += 1
        return res







if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = 'ABC'
    solution = Solution()
    result = solution.minWindow(s,t)
    print(result)