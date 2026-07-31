class Solution:
    def find(self,nums:List[int],start:int,end:int,target:int)->int:
        l=start
        r = end
        #print("l->",l,"r->",r)
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l=mid+1
            else:
                r=mid-1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        l =0
        r = len(nums)-1
        while(l<r):
            mid = (l+r)//2
            if(nums[mid]<=nums[r]):
                r = mid
            else:
                l=mid+1
        print(nums[l],"l->",l,"r->",r)
        print("first condition")
        ans =  self.find(nums,0,l-1,target)
        if(ans!=-1):
            return ans
        print("second condition")
        return self.find(nums,l,len(nums)-1,target)