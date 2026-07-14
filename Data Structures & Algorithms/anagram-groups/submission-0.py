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
        my_map = {}
        for s in strs:
            flag=False
            for item in my_map:
                if self.isSame(item,s):
                    my_map[item].append(s)
                    flag=True
                    break
            if(flag==False):
                my_map.setdefault(s, []).append(s)
        return list(my_map.values())
        