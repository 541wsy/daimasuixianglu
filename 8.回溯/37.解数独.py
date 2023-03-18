class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(rowind, colind, k, board):
            #判断同一行是否有相同数字
            if k in board[rowind]:
                return False
            #判断同一列是否有相同数字
            for row in board:
                if row[colind] == k:
                    return False
            #判断同个九宫格是否有相同数字
            ##rowind位于第几个九宫格
            ##colind位于第几个九宫格
            row9 = rowind // 3
            col9 = colind // 3
            #提取该九宫格元素
            tmp = []
            for i in range(row9 * 3, (row9 + 1) * 3):
                for j in range(col9 * 3, (col9 + 1) * 3):
                    if board[i][j] == k:
                        return False

            return True

        #递归函数返回值是bool，这样可以控制找到一个解立刻返回
        def backtraking(board):
            #两层for循环，找到每个空白位置
            for i in range(len(board)):
                for j in range(len(board[0])):
                    #如果搜索到空格
                    if board[i][j] == '.':
                        #循环依次填入9个数字，判断是否合法
                        for k in range(1,10):
                            #如果合法,放入数字
                            if isvalid(i, j, str(k), board):
                                board[i][j] = str(k)
                                #递归，只要找到解，立刻返回
                                if backtraking(board):
                                    return True
                                #回溯
                                board[i][j] = '.'
                        #如果当前空格9个数字都不合法,返回False，进行回溯
                        return False
            #搜索完全部棋盘，返回True
            return True
        backtraking(board)
        return board