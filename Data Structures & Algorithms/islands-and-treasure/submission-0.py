from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        def addcell(row:int,col:int):
            if(row<0 or col<0 or row >= ROWS or col >= COLS or (row,col) in visited or grid[row][col]==-1):
                return
            q.append([row,col])
            visited.add((row,col))
        
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]==0):
                    q.append([i,j])
                    visited.add((i,j))
        dist = 0
        while(q):
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addcell(r+1,c)
                addcell(r,c+1)
                addcell(r-1,c)
                addcell(r,c-1)
            dist+=1

        
