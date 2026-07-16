class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        start = []
        max1=0
        for num in nums:
            s.add(num)
        for num in nums:
            if(num-1 not in s):
                start.append(num)
        print(start)
        curr_max=1
        for numbers in start:
            while(numbers+1 in s):
                curr_max+=1
                numbers+=1
                print("number",numbers ,"curr_max",curr_max)
            if(curr_max>max1):
                max1 = curr_max
            curr_max = 1
            print(curr_max,max1)
        return max1
        