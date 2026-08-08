class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fre =[0]*len(nums)
        for i in range(len(nums)):
            if(fre[nums[i]]>0):
                return nums[i]
            else:
                fre[nums[i]]=1