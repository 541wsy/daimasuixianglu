class Solution:
    def partitionLabels(self, s):
        # s转化为区间列表
        from collections import defaultdict
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)

        #转化为每个字母的覆盖范围区间
        intervals = []
        for val in dic.values():
            intervals.append([min(val), max(val)])
        # intervals按照左区间排序
        intervals.sort(key=lambda x: x[0])
        #cuts存放每次的分割点index
        cuts = [0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i - 1][1]:
                cuts.append(intervals[i][0])
            else:
                intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        cuts.append(len(s))
        #将分割点index转化为分割的每段长度
        result = []
        for i in range(1, len(cuts)):
            result.append(cuts[i] - cuts[i - 1])
        return result


s = 'ababcbacadefegdehijhklij'
solution = Solution()
solution.partitionLabels(s)