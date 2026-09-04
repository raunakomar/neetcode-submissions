class Solution:
    def __init__(self):
        self.visited = []
    def check(self,board:List[List[str]],word:str,position:int,x:int,y:int,visited:List[List[int]])->bool:
        if(position==len(word)):
            return True
        if(x<0 or x>=len(board) or y<0 or y>=len(board[0])):
            return False
        #if(board[x][y]==word[position]):
        #   return True
        if(visited[x][y]==0 and word[position]==board[x][y]):
            visited[x][y]=1
            found = (
            self.check(board, word, position + 1, x + 1, y, visited)
            or self.check(board, word, position + 1, x - 1, y, visited)
            or self.check(board, word, position + 1, x, y + 1, visited)
            or self.check(board, word, position + 1, x, y - 1, visited)
            )
            visited[x][y] = 0   # <-- BACKTRACK
            return found
        else:
            return False
    def findS(self,board:List[List[str]],word:str)->List[List[int]]:
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==word[0]):
                    ans.append([i,j])
        return ans
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = self.findS(board,word)
        rows = len(board)
        cols = len(board[0])
        #arr = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(len(start)):
            arr = [[0 for _ in range(cols)] for _ in range(rows)]
            if(self.check(board,word,0,start[i][0],start[i][1],arr)):
                return True
        return False