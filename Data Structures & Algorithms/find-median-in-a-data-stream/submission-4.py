import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.sum = 0
        self.count = 0

    def rebalance(self,source:List[int],dest:List[int],flag:bool)->None:
        #if(len(dest)==0):
            #print("no element in dest , taking from source",source[0])
        #else:
            #print("taking ",source[0],"to destination",dest[0])
        if(flag):
            heapq.heappush(dest,(-1*heapq.heappop(source)))
        else:
            heapq.heappush(dest,(-1*heapq.heappop(source)))
        #print("new source ",source[0],"new destination",dest[0])

    def addNum(self, num: int) -> None:
        if(self.count==0):
            self.maxheap.append(-1*num)
        else:
            if(num<(-1*self.maxheap[0])):
                #print("inserting ",num,"in maxheap left side")
                heapq.heappush(self.maxheap,(-1*num))
            else:
                #print("inserting ",num,"in minheap right side")
                heapq.heappush(self.minheap,num)
        self.sum += num
        self.count += 1
        if(len(self.maxheap)- len(self.minheap)>1):
            #print("rebalancing from left to right")
            self.rebalance(self.maxheap,self.minheap,"True")
        if(len(self.minheap)-len(self.maxheap)>1):
            #print("rebalancing from right to left")
            self.rebalance(self.minheap,self.maxheap,"False")

    def findMedian(self) -> float:
        if(self.count%2==0):
            return ((-1*self.maxheap[0])+self.minheap[0])/2
        else:
            if(len(self.maxheap)>len(self.minheap)):
                return (-1*self.maxheap[0])
            else:
                return self.minheap[0]
        
        
