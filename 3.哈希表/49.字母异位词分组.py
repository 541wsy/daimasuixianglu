class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 此题关键在于哈希key的设计，要找到异构词本质不变的性质
        # 1.异构词排序后字符串相同
        # 2.异构词的字母计数字典相同

        # # 方法1：排序
        # from collections import defaultdict
        # ## 对每个字符串排序，排序后的字符串就不是异位字符串，用一个字典计数
        # dic = defaultdict(list)
        # for string in strs:
        #     sort_str = "".join(sorted(string))
        #     #注：sorted可以对（list, tuple,dict,set,str）进行排序，返回一个list
        #     #"".join()表示将括号内传入list的每个元素用""进行连接，返回一个字符串
        #     #这种写法是对字符串排序返回一个字符串的标准写法
        #     dic[sort_str].append(string)
        # return dic.values()

        # 方法2：计数
        from collections import defaultdict

        dic = defaultdict(list)

        for string in strs:
            # 计算每个string的字母计数哈希表，用数组实现
            count_hash = [0] * 26
            for ch in string:
                count_hash[ord(ch) - ord('a')] += 1

            dic[tuple(count_hash)].append(string)  # 注意list是可变对象不可以做key，转成元组才可以
        return dic.values()

        ## 注：python的可变对象和不可变对象，只有不可变对象才可以hash
        # 不可变对象包括：bool（布尔）、int（整数）、float（浮点数）、str（字符串）、tuple（元组）、frozenset（不可变集合）
        # 可变对象包括：list（列表）、set（集合）、dict（字典）





