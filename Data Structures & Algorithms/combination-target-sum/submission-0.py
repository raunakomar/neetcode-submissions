class Solution:
    #build array and curr sum 
    #if curr sum > target then return
    # elif cur sum==target then add
    # 2-> 2
    # 2->5
    #2->6
    #2->9
    def __init__(self):
        self.ans = []
    def findSum(self,nums:List[int],arr:List[int],currSum:int,target:int,position:int)->None:
        if(target<currSum):
            return
        if(target==currSum):
            self.ans.append(arr.copy())
            return
        for i in range(position,len(nums)):
            arr.append(nums[i])
            currSum+=nums[i]
            self.findSum(nums,arr,currSum,target,i)
            arr.remove(nums[i])
            currSum-=nums[i]
            

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        self.findSum(nums,arr,0,target,0)
        return self.ans