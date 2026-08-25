import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [0]*len(stones)
        for i in range(len(stones)):
            heap[i]=(stones[i]*-1)

        heapq.heapify(heap)
        while(len(heap)>1):
            w1 = (heapq.heappop(heap)*-1)
            w2 = (heapq.heappop(heap)*-1)
            weight = w1-w2
            if(weight<0):
                heapq.heappush(heap,weight)
            elif(weight>0):
                heapq.heappush(heap,weight*-1)
        if(len(heap)==1):
            return heapq.heappop(heap)*-1
        else:
            return 0
        
