class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        # 与49题很类似
        ## 循环所有可能的异位词，异位词可以通过计数或者排序判断,如果是异位词，将索引添加到dic
        # 方法1：排序（排序做法不通过，可能是因为当字符串很长，时间复杂度过大）
        # from collections import defaultdict

        # dic = defaultdict(list)

        # #循环所有可能的异位词
        # for start in range(len(s) - len(p) + 1):
        #     cand_str = s[start:start+len(p)]
        #     cand_str_sort = ''.join(sorted(cand_str)) #排序字符串
        #     dic[cand_str_sort].append(start)
        # p_sort = ''.join(sorted(p)) #将字符串p排序，dic[p_sort]对应的value即时结果
        # return dic[p_sort]

        # 方法2：计数（这个也超时）
        # if len(s) < len(p):
        #     return []
        # from collections import defaultdict
        # dic = defaultdict(list)

        # for start in range(len(s) - len(p) + 1):
        #     cand_str = s[start:start+len(p)]
        #     #为cand_str创造一个字母计数哈希表
        #     count = [0] * 26
        #     for ch in cand_str:
        #         count[ord(ch) - ord('a')] += 1
        #     dic[tuple(count)].append(start)

        # #为p创造计数字典
        # count_p = [0] * 26
        # for ch in p:
        #     count_p[ord(ch) - ord('a')] += 1
        # return dic[tuple(count_p)]

        # 方法3：计数方法优化
        ## 方法2做了很多重复工作，在移动滑动窗口的时候，cand_str的计数字典变化只需要关注头尾指针即可，不需要把中间的字母重新计数，所以方法2导致了超时
        from collections import defaultdict
        result = []
        # p的计数字典
        count_p = [0] * 26  # p的key，即目标key
        for ch in p:
            count_p[ord(ch) - ord('a')] += 1

        # 初始化cand_str计数字典
        cand_count = [0] * 26
        for ch in s[0:len(p)]:
            cand_count[ord(ch) - ord('a')] += 1
        # 对初始结果进行判断
        if count_p == cand_count:
            result.append(0)
        # 如果初始结果不是异构词，继续滑动窗口
        for ind in range(len(s) - len(p)):  # ind位置是本轮循环要删除的，所以循环到len(s)-len(p)
            # 计数字典删除ind位置的计数，添加ind + len(p)的计数结果
            cand_count[ord(s[ind]) - ord('a')] -= 1
            cand_count[(ord(s[ind + len(p)]) - ord('a'))] += 1
            if cand_count == count_p:
                result.append(ind + 1)
        return result


s = "abab"
p = "ab"
solution = Solution()
result = solution.findAnagrams(s, p)