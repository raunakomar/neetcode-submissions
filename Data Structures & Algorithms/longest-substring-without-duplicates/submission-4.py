class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        i = 0
        if(len(s)==0):
            return 0
        st.add(s[i])
        j = i+1
        max_l = 1
        while(j<len(s)):
            if(s[j] in st):
                while(s[i]!=s[j]):
                    if(len(st)>max_l):
                        max_l=len(st)
                    print("current i->",i,"s[i]->",s[i])
                    st.remove(s[i])
                    i+=1
                print("current i->",i,"current j->",j)
                i+=1
                j+=1
            else:
                print("current j->",j,"s[j]->",s[j])
                st.add(s[j])
                j+=1
        return max(max_l,len(st))

