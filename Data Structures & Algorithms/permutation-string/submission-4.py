class Solution:
    def checkMap(self,hs1:{},hs2:{})->bool:
        for key, value in hs1.items():
            print(key, value)
            if(key in hs2.keys()):
                if(hs1[key]!=hs2[key]):
                    return False
            else:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hs1 = {}
        hs2 = {}
        if(len(s1)>len(s2)):
            return False
        for i in range(0,len(s1)):
            hs1[s1[i]] = hs1.get(s1[i],0) + 1
            hs2[s2[i]] = hs2.get(s2[i],0) + 1
        i = 0
        flag = False
        j = i+len(s1)-1
        while(i+len(s1)<=len(s2)):
            print("current i->",i,"j->",j)
            for key, value in hs2.items():
                print(key, value)
            print("checking map")
            if(self.checkMap(hs1,hs2)):
                return True
            else:
                hs2[s2[i]]-=1
                i+=1
                j+=1
                if(j<len(s2)):
                    hs2[s2[j]] = hs2.get(s2[j],0) + 1
                else:
                    break
        return False