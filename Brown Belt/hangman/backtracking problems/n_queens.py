# each queen will be on a different column and a different row
#we use the sets posDiag and negDiag to check the diagonals to ensure that no 2 queens are on the same diagonals
def solve_n_queens(n: int):
    col = set()
    posDiag = set() # (r + c)
    negDiag = set() # (r - c)

    res=[]
    board=[["."]*n for i in range(n)]

    def backtracking(r):
        if r==n:
            copy=["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtracking(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtracking(0)
    return res

n=4
print(solve_n_queens(n))
