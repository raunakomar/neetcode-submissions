class Solution:
    def __init__(self):
        self.ans = []
    def pal(self,s:str,j:int,i:int)->bool:
        if(j>=len(s) or i>=len(s) or j<0 or i<0):
            return False
        while(j!=i and j<i):
            if(s[j]!=s[i]): 
                return False 
            j+=1
            i-=1
        return True

    def getPal(self, s: str, j: int, arr: List[List[str]]) -> None:
        if j >= len(s):
            self.ans.append(arr.copy())
            return
        print("checking for j=",j)
        for i in range(j, len(s)):
            if self.pal(s, j, i):
                arr.append(s[j:i+1])
                self.getPal(s, i + 1, arr)
                arr.pop()

        return  


    def partition(self, s: str) -> List[List[str]]:
        if (len(s)==0):
            return self.ans
        self.getPal(s,0,[])
        return self.ans
        