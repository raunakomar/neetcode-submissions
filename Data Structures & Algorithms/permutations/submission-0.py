class Solution:
    def __init__(self):
        self.ans = []
    def swap(self,nums:List[int],i:int,j:int)->None:
        temp = nums[j]
        nums[j]=nums[i]
        nums[i]=temp
    def genperm(self,nums:List[int],position:int,arr:List[int])->None:
        if(len(nums)==position):
            self.ans.append(arr.copy())
        for i in range(position,len(nums)):
            self.swap(nums,position,i)
            arr.append(nums[position])
            self.genperm(nums,position+1,arr)
            arr.pop()
            self.swap(nums,position,i)
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        self.genperm(nums,0,arr)
        return self.ans