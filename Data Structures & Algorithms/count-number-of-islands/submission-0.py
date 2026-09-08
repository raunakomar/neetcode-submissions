class Solution:
    def __init__(self):
        self.ans= 0
    def check(self,v:List[List[bool]],grid:List[List[str]])->bool:
        print("checking")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1" and v[i][j]==False):
                    print("found one difference")
                    return False
        print("returning no issue")
        return True
    def getone(self,v:List[List[bool]],grid:List[List[str]])->List[int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1" and v[i][j]==False):
                    return [i,j]
        return None
    def find(self,grid:List[List[str]],i:int,j:int,v:List[List[bool]])->None:
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0])):
            return
        if(grid[i][j]=="0" or v[i][j]==True):
            return
        v[i][j] = True
        self.find(grid,i+1,j,v)
        self.find(grid,i-1,j,v)
        self.find(grid,i,j+1,v)
        self.find(grid,i,j-1,v)
    def numIslands(self, grid: List[List[str]]) -> int:
       # get a 2d visited array
       # find first 1 
       # keep on moving all the direction
       # if 1 and visited [0] then mark visited
       # if 0, or visited = true then return 
       rows = len(grid)
       cols = len(grid[0])

       v = [[False for _ in range(cols)] for _ in range(rows)]
       while(self.check(v,grid)==False):
        i,j = self.getone(v,grid)
        print("found i",i," j",j)
        self.ans+=1
        self.find(grid,i,j,v)
       return self.ans