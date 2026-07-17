class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_arr = []
        for c in s.lower():
            if((c>='a' and c<='z') or (c>='0' and c<='9')):
                char_arr.append(c)
        print(char_arr)
        i = 0
        j = len(char_arr)-1
        while(i<=j):
            if(char_arr[i]!=char_arr[j]):
                return False
            i+=1
            j-=1
        return True