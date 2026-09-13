from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited =set()
        q = deque()
        def markrotten(i:int,j:int):
            if(i<0 or j<0 or i>=ROWS or j>=COLS or (i,j) in visited or grid[i][j]==0):
                return
            visited.add((i,j))
            q.append((i,j))
        def checkfresh()->bool:
            for i in range(ROWS):
                for j in range(COLS):
                    if((i,j) not in visited and grid[i][j]==1):
                        return True
            return False
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]==2):
                    q.append((i,j))
                    visited.add((i,j))

        time = 0
        while(len(q)>0):
            for i in range(len(q)):
                x,y = q.popleft()
                markrotten(x+1,y)
                markrotten(x,y+1)
                markrotten(x-1,y)
                markrotten(x,y-1)
            time+=1
        yes = checkfresh()
        if(yes):
            return -1
        else:
            return max(0, time - 1)