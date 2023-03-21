class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        tmpmerge = intervals[0]

        result = []
        for i in range(1, len(intervals)):
            # 如果重叠了
            if intervals[i][0] <= tmpmerge[1]:
                tmpmerge = [tmpmerge[0], max(tmpmerge[1], intervals[i][1])]
            else:  # 如果不重合，把tmpmerge放入result
                result.append(tmpmerge)
                tmpmerge = intervals[i]
        #还要把最后一个tmpmerge加入result
        result.append(tmpmerge)
        return result
solution = Solution()
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
result = solution.merge(intervals)