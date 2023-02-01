class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        result = [[0] * n for _ in range(n)]  # 初始化全0矩阵

        startx, starty = 0, 0  # 起始位置初始化
        offset = 1  # 每一圈缩减单位，初始为1
        count = 1  # 赋值数值
        for loop in range(n // 2):  # 完整螺旋圈数
            # 循环第一条边
            for j in range(starty, n - offset):
                result[startx][j] = count
                count += 1
            # 循环第二条边
            for i in range(startx, n - offset):
                result[i][n - offset] = count
                count += 1
            # 循环第三条边
            for j in range(n - offset, starty, -1):
                result[n - offset][j] = count
                count += 1
            # 循环第四条边
            for i in range(n - offset, startx, -1):
                result[i][starty] = count
                count += 1
            # 一圈循环结束，更新startx,starty,offset
            startx += 1
            starty += 1
            offset += 1

        # 如果是奇数，多进行一次赋值
        if n % 2 == 1:
            result[startx][starty] = count

        return result


n = 3
solution = Solution()
result = solution.generateMatrix(n)
print(result)