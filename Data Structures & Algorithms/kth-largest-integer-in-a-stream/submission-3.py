import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.nums = nums
        if(len(nums)>0):
            heapq.heappush(self.heap,nums[0])
        for i in range(1,len(nums)):
            if(len(self.heap)==k):
                print("limit reached")
                if(nums[i]<self.heap[0]):
                    continue
                heapq.heappop(self.heap)
                print("now limit ",len(self.heap))
            heapq.heappush(self.heap,(nums[i]))
            print("inserted ",nums[i],"heap length",len(self.heap))
        for i in range(len(self.heap)):
            print("printing",self.heap[i])

    def add(self, val: int) -> int:
        if(len(self.heap)>0 and val<self.heap[0]):
            return self.heap[0]
        if(len(self.heap)==self.k):
            heapq.heappop(self.heap)
        heapq.heappush(self.heap,(val))
        return self.heap[0]
