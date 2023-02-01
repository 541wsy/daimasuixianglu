class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 求行数，列数
        row = len(matrix)
        col = len(matrix[0])
        # 初始化
        startx, starty = 0, 0
        offset = 1

        result = []

        while startx < row - offset and starty < col - offset:
            for j in range(starty, col - offset):
                result.append(matrix[startx][j])
            for i in range(startx, row - offset):
                result.append(matrix[i][col - offset])
            for j in range(col - offset, starty, -1):
                result.append(matrix[row - offset][j])
            for i in range(row - offset, startx, -1):
                result.append(matrix[i][starty])

            # 一圈循环结束，更新startx, starty, offset
            startx += 1
            starty += 1
            offset += 1
        else:  # 当螺旋不满一圈时
            if row - offset == startx: #剩下的螺旋是水平
                for j in range(starty, col - offset + 1):
                    result.append(matrix[startx][j])
            if col - offset == starty: #剩下的螺旋是竖直
                for i in range(startx, row - offset + 1):
                    result.append(matrix[i][starty])

        return result


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution = Solution()
result = solution.spiralOrder(matrix)