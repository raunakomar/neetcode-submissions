class Solution:
    def __init__(self):
        self.ans =[]
    def getP(self,n:int,length:int,opn:int,arr:List[str])->None:
        if(length>n or opn>length or opn <0):
            return
        if(length==n and opn==0):
            s = ""
            for i in range(len(arr)):
                s+=arr[i]
            self.ans.append(s)
            return
        if(length==n and opn>0):
            counter = 0
            while(opn>0):
                arr.append(')')
                counter+=1
                opn-=1
            s = ""
            for i in range(len(arr)):
                s+=arr[i]
            self.ans.append(s)
            while(counter>0):
                arr.pop()
                counter-=1
            return
        arr.append('(')
        self.getP(n,length+1,opn+1,arr)
        arr.pop()
        arr.append(')')
        self.getP(n,length,opn-1,arr)
        arr.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        length = 1
        arr=[]
        arr.append('(')
        answer = []
        self.getP(n,length,1,arr)
        for i in range(len(self.ans)):
            print(self.ans[i])
        return self.ans