class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []
        # 创建一个ticket映射字典，key是出发机场，value是到达机场
        from collections import defaultdict
        dic = defaultdict(list)

        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])

        # ticket映射字典中的列表要排序
        for ariport in list(dic.keys()):
            dic[ariport].sort()

            # 从JFK出发
        path.append('JFK')

        def backtracking(startair):
            if len(path) == len(tickets) + 1:
                return True

            for _ in dic[startair]:  # 这里不能for endair in dic[startair]
                endair = dic[startair].pop(0)  # 删除到达机场，避免重复
                path.append(endair)
                # 递归
                ##只要找到就返回
                if backtracking(endair):
                    return True
                # 回溯
                path.pop()
                dic[startair].append(endair)  # 此处不需要排序，因为不会再取到了

        backtracking('JFK')
        return path


solution = Solution()
tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
result = solution.findItinerary(tickets)