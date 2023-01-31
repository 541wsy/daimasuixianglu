from collections import Counter
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = Counter()
        i = 0
        number = 0
        for j,x in enumerate(fruits):
            count[x] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    count.pop(fruits[i])
                i += 1

            number_tmp = j - i + 1
            number = max(number, number_tmp)
        return number
fruits = [0,1,2,2]
solution = Solution()
result = solution.totalFruit(fruits)