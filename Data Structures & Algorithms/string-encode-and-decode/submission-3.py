class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            for i in s:
                string+=i
                #print(string)
            string +='\u00E9'
        return string

    def decode(self, s: str) -> List[str]:
        string = []
        i = 0
        str1 = ""
        while i<len(s):
            if(s[i]!='\u00E9'):
                str1+=s[i]
                #print(str1)
            else:
                string.append(str1)
                #print(string)
                str1=""
            i=i+1
        return string

