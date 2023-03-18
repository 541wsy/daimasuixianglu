class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = []
        result = []
        # 初始化棋盘
        chessboard = [['.'] * n for _ in range(n)]

        def isvalid(rowind, colind, chessboard):
            # 判断是否同列
            for row in chessboard:
                if row[colind] == 'Q':
                    return False
            # 判断左上角
            cur_row = rowind - 1
            cur_col = colind - 1

            while cur_row >= 0 and cur_col >= 0:
                if chessboard[cur_row][cur_col] == 'Q':
                    return False
                cur_row -= 1
                cur_col -= 1

            # 判断右上角
            cur_row = rowind - 1
            cur_col = colind + 1

            while cur_row >= 0 and cur_col < n:
                if chessboard[cur_row][cur_col] == 'Q':
                    return False
                cur_row -= 1
                cur_col += 1
            return True

        def backtraking(rowind, chessboard):
            # rowind表示当前是第几行
            if rowind == n:
                tmp = []
                for i in range(n):
                    tmp.append(''.join(chessboard[i]))
                result.append(tmp)
                return

            for j in range(n):  # 遍历列
                # 如果当前放置皇后合法
                if isvalid(rowind, j, chessboard):
                    chessboard[rowind][j] = 'Q'
                    # 递归
                    backtraking(rowind + 1, chessboard)
                    # 回溯
                    chessboard[rowind][j] = '.'

        backtraking(0, chessboard)
        return result