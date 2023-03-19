class Solution:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0

        path = []
        for i in range(len(prices)):
            # 首尾情况单独
            if i == 0:
                if prices[i + 1] > prices[i]:
                    path.append(prices[i])
            elif i == len(prices) - 1:
                if prices[i] > prices[i - 1]:
                    path.append(prices[i])
            # 非首尾
            else:
                # 找波谷
                if prices[i] <= prices[i - 1] and prices[i] < prices[i + 1]:
                    path.append(prices[i])
                elif prices[i] > prices[i - 1] and prices[i] >= prices[i + 1]:
                    path.append(prices[i])
        num = len(path) // 2  # 有几段交易
        result = 0
        for i in range(num):
            result += (path[2 * i + 1] - path[2 * i])
        return result

solution = Solution()
prices = [7,1,5,3,6,4]
result = solution.maxProfit(prices)
print('f')