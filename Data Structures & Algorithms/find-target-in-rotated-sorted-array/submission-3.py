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
        if(nums[l]==target):
            return l
        elif(l!=0 and nums[0]<=target):
            print("first condition")
            return self.find(nums,0,l-1,target)
        else:
            print("second condition")
            return self.find(nums,l,len(nums)-1,target)