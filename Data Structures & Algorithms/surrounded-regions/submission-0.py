from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if(len(board)==0):
            return
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()
        print("executed line 7")
        def dfs(i,j)->None:
            if(i<0 or j<0 or i>=ROWS or j>=COLS or board[i][j]=="X" or board[i][j]=="-1"):
                return
            print("making change in ",i,j)
            board[i][j]="-1"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        #insert upper row
        for j in range(COLS):
            if board[0][j] == "O":
                print("executed line 20")
                dfs(0, j)

            if board[ROWS - 1][j] == "O":
                print("executed line 24")
                dfs(ROWS - 1, j)

        for i in range(ROWS):
            if board[i][0] == "O":
                print("executed line 29")
                dfs(i, 0)

            if board[i][COLS - 1] == "O":
                print("executed line 33")
                dfs(i, COLS - 1)
        
        for i in range(len(q)):
            x,y = q.popleft()
            dfs(x,y)
        for i in range(ROWS):
            for j in range(COLS):
                if(board[i][j]=="O"):
                    board[i][j]="X"
                if(board[i][j]=="-1"):
                    board[i][j]="O" 
