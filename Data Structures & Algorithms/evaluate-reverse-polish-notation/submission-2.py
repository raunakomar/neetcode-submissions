class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if(tokens[i]=='+'):
                if(len(stk) < 2):
                    return -1
                first = int(stk.pop())
                second = int(stk.pop())
                stk.append(first+second)
            elif(tokens[i]=='-'):
                if(len(stk)<2):
                    return -1
                first = int(stk.pop())
                second = int(stk.pop())
                stk.append(second-first)
            elif(tokens[i]=='*'):
                if(len(stk)<2):
                    return -1
                first = int(stk.pop())
                second = int(stk.pop())
                result = first * second
                stk.append(result)
            elif(tokens[i]=='/'):
                if(len(stk)<2):
                    return -1
                first = int(stk.pop())
                second = int(stk.pop())
                stk.append(second/first)
            else:
                stk.append(tokens[i])
        return int(stk.pop())