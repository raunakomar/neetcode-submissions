class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0]*26
        arr2 = [0]*26
        if len(s)!=len(t):
            return False
        for ch in s:
            arr1[ord(ch) - ord('a')] += 1
        for ch in t:
            arr2[ord(ch) - ord('a')] += 1
        for i in range(26):
            if arr1[i]!=arr2[i]:
                return False

        return True
        

        