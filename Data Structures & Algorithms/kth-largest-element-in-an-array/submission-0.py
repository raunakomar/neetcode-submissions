import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])

        l = len(nums)-k
        while(l>0):
            heapq.heappop(heap)
            l-=1

        return heapq.heappop(heap)