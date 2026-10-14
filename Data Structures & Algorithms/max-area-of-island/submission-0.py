class Solution:
    def __init__(self):
        self.ans= 0
    def check(self,v:List[List[bool]],grid:List[List[int]])->bool:
        print("checking")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1 and v[i][j]==False):
                    print("found one difference")
                    return False
        print("returning no issue")
        return True
    def getone(self,v:List[List[bool]],grid:List[List[int]])->List[int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1 and v[i][j]==False):
                    return [i,j]
        return None
    def find(self,grid:List[List[int]],i:int,j:int,v:List[List[bool]])->int:
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0])):
            return 0
        if(grid[i][j]==0 or v[i][j]==True):
            return 0
        v[i][j] = True
        l1 = self.find(grid,i+1,j,v)
        l2 = self.find(grid,i-1,j,v)
        l3 = self.find(grid,i,j+1,v)
        l4 = self.find(grid,i,j-1,v)
        return (1+l1+l2+l3+l4)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       rows = len(grid)
       cols = len(grid[0])
       length = 0
       v = [[False for _ in range(cols)] for _ in range(rows)]
       while(self.check(v,grid)==False):
        i,j = self.getone(v,grid)
        print("found i",i," j",j)
        self.ans+=1
        l = self.find(grid,i,j,v)
        length = max(l,length)
       return length