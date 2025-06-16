class Solution:
    def solveNQueens(self, n: int) :

        solutions=[]

        def is_safe(board,row,col):
            for i in range(row):
                if board[i][col]=='Q':
                    return False
            i=row-1
            j=col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1

            i=row-1
            j=col+1

            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1

            return True

        def solve_n_queens(board,row):
            if row==n:
                solution=["".join(row)for row in board]
                solutions.append(solution)
                return
            for col in range(n):
                if is_safe(board,row,col):
                    board[row][col]='Q'
                    solve_n_queens(board,row+1)
                    board[row][col]='.'

        board=[['.' for _ in range(n)]for _ in range(n)]
        solve_n_queens(board,0)
        return solutions
        