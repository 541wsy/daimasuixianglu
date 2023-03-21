class Solution:
    def candy(self, ratings):
        if len(ratings) == 1:
            return 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy1[i] = candy1[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy2[i] = candy2[i + 1] + 1

solution = Solution()
ratings = [1,2,87,87,87,2,1]
result = solution.candy(ratings)