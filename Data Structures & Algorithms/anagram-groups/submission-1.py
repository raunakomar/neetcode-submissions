class Solution:
    def isSame(self,str1:str , str2:str)->bool:
        arr1 = [0]*26
        arr2 = [0]*26
        for s in str1:
            arr1[ord(s)-ord('a')]+=1
        for s in str2:
            arr2[ord(s)-ord('a')]+=1
        return arr1==arr2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())
        