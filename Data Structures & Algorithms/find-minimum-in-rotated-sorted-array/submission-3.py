class Solution:
    def findMin(self, nums: List[int]) -> int:
        #mid is greater than first then rotation point is in right
        #mid is less than first then rotation point is in left
        #find rotation point
        #return nums[mid]
        l = 0
        r =len(nums)-1
        while(l<=r):
            mid = (r+l)//2
            if(mid!=0 and nums[mid]<nums[mid-1]):
                return nums[mid]
            elif(mid!=len(nums)-1 and nums[mid]>nums[mid+1]):
                return nums[mid+1]
            elif(nums[mid]<nums[l]):
                r = mid-1
            elif(nums[mid]>nums[l]):
                l = mid+1
            else:
                break
        return nums[0]