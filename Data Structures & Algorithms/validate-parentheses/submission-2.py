class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(0,len(s)):
            print("s[i]->",s[i])
            print(stk)
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                stk.append(s[i])
            elif(s[i]==')'):
                if(len(stk)==0 or stk.pop()!='('):
                    return False
            elif(s[i]==']'):
                if(len(stk)==0 or stk.pop()!='['):
                    return False
            elif( s[i]=='}'):
                if(len(stk)==0 or stk.pop()!='{'):
                    return False
        if(len(stk)!=0):
            return False
        else:
            return True