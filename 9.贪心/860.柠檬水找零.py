class Solution:
    def lemonadeChange(self, bills):
        pocket = {
            '5': 0,
            '10': 0
        }

        for bill in bills:
            if bill == 5:
                pocket['5'] += 1
            elif bill == 10:
                # 如果没有5元了
                if pocket['5'] == 0:
                    return False

                pocket['5'] -= 1
                pocket['10'] += 1
            else:  # 优先找10块，因为5块可以找给10元的单（贪心）
                if pocket['10'] >= 1 and pocket['5'] >= 1:
                    pocket['5'] -= 1
                    pocket['10'] -= 1
                # 不能找10块，考虑找3个五块
                elif pocket['5'] >= 3:
                    pocket['5'] -= 3
                # 失败
                else:
                    return False

        return True
bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
solution = Solution()
result = solution.lemonadeChange(bills)