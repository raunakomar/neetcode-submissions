class Solution:
    def isValid(self,rate:int,hour:int,piles:List[int])-> bool:
        total_hours = 0
        for i in range(len(piles)):
            total_hours += (piles[i] + rate - 1) // rate
            print(total_hours)
        print("total_hours",total_hours)
        if(total_hours<=hour):
            return True
        else:
            return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_i = 0
        for i in range((len(piles))):
            if(max_i<piles[i]):
                max_i = piles[i]

        l = 0
        r = max_i
        valid_rate = 0
        while(l<=r):
            mid = (l+r)//2
            print("mid is ",mid)
            if(mid==0):
                break
            elif(self.isValid(mid,h,piles)):
                print("is valid for ",mid)
                valid_rate = mid
                r= mid-1
            else:
                print("is invalid for ",mid)
                l = mid+1
        if(r==max_i):
            if(self.isValid(r,h,piles)):
                return True
        return valid_rate