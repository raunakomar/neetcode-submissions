class Solution:
    def __init__(self):
        self.mapper = {}
        self.mapper["2"]= ['a','b','c']
        self.mapper["3"]= ['d','e','f']
        self.mapper["4"]= ['g','h','i']
        self.mapper["5"]= ['j','k','l']
        self.mapper["6"]= ['m','n','o']
        self.mapper["7"]= ['p','q','r','s']
        self.mapper["8"]= ['t','u','v']
        self.mapper["9"]= ['w','x','y','z']
    
    def getN(self,digits:str)->List[str]:
        ans = []
        if(len(digits)==1):
            for i in range(len(self.mapper[digits])):
                ans.append(self.mapper[digits][i])
            return ans
        sub_ans = self.getN(digits[1:])
        for i in range(len(self.mapper[digits[0]])):
            for j in range(len(sub_ans)):
                ans.append(self.mapper[digits[0]][i]+sub_ans[j])
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0):
            return []
        return self.getN(digits)
