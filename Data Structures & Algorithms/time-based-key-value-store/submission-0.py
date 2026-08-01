from collections import defaultdict

class TimeMap:

    def binarySearch(self,nums:list[int],target)->int:
        l=0
        r=len(nums)-1
        ans = -1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                ans = mid
                return mid
            elif(nums[mid]<target):
                ans = mid
                l=mid+1
            else:
                r=mid-1
        return ans
    

    def __init__(self):
        self.my_map_val = defaultdict(list)
        self.my_map_time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_map_val[key].append(value)
        self.my_map_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.my_map_time):
            return ""
        
        index = self.binarySearch(self.my_map_time[key],timestamp)
        if index != -1:
            return self.my_map_val[key][index]
        else :
            return ""

