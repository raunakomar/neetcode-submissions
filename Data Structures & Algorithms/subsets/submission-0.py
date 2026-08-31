class Solution:
    def __init__(self):
        self.ans = []
    def getSubsets(self,nums:List[int],arr:List[int],position:int)->None:
        if(position==len(nums)):
            self.ans.append(arr.copy())
            return
        #take part
        arr.append(nums[position])
        for i in range(len(arr)):
            print(arr[i])
        self.getSubsets(nums,arr,position+1)
        arr.remove(nums[position])
        for i in range(len(arr)):
            print(arr[i])
        self.getSubsets(nums,arr,position+1)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        self.getSubsets(nums,arr,0)
        return self.ans