class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stk =[]
        for i in range(len(temperatures)):
            if(len(stk)==0):
                stk.append(i)
            # if top of stack is less than current
            # remove top and put gap in result
            # keep on doing untill stak is empty or top is greater than current
            elif(temperatures[stk[-1]]<temperatures[i]):
                while(len(stk)>0 and temperatures[stk[-1]]<temperatures[i]):
                    res[stk[-1]] = i-stk[-1]
                    stk.pop()
                stk.append(i)
            elif(temperatures[stk[-1]]>=temperatures[i]):
                stk.append(i)
        return res