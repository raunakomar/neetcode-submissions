class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       my_set = set()
       a = -1
       b = -1
       for num in nums:
        my_set.add(num)
       for num in nums:
        if target-num in my_set:
            a = num
            b = target-num
       return sorted([nums.index(a), len(nums) - 1 - nums[::-1].index(b)])
        