class Solution:

    def encode(self, strs: List[str]) -> str:
        string =""
        for s in strs:
            l = len(s)
            string+=str(l)
            string+="#"
            for i in s:
                string+=i
        #print(string)
        return string

    def decode(self, s: str) -> List[str]:
        str1 = []
        i = 0
        length=''
        while(i<len(s)):
            
            if s[i]!='#':
                length+=s[i]
                #print(length)
                i+=1
            else:
                i+=1
                string=s[i:(i+int(str(length)))]
                print(string)
                str1.append(string)
                i+=int(length)
                length=''
            string=""
        return str1

