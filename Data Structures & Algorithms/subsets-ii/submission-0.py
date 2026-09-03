class Solution:
    def __init__(self):
        self.ans = []
    
    def getSubSet(self,nums:List[int],position:int,arr:List[int])->None:
        if(position==len(nums)):
            self.ans.append(arr.copy())
            return
        arr.append(nums[position])
        self.getSubSet(nums,position+1,arr)
        arr.pop()
        while(position+1<len(nums) and nums[position]==nums[position+1]):
            position=position+1
        self.getSubSet(nums,position+1,arr)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        self.getSubSet(nums,0,arr)
        return self.ans