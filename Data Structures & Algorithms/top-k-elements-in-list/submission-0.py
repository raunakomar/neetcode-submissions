import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        pq = []
        for i in nums:
            if i in my_map:
                my_map[i]+=1
            else :
                my_map[i]=1
        for item in my_map:
            heapq.heappush(pq,(-1*my_map[item],item))
        result =[]
        i=0
        while i<k:
            priority,value = heapq.heappop(pq)
            result.append(value)
            i=i+1
        return result

        
        