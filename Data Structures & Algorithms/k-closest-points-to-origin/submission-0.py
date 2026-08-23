import heapq
class Solution:
    def distanceFromOrigin(self,point:List[int])->int:
        x = point[0]
        y = point[1]
        sq = ((x*x) + (y*y))
        return sq
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        ans = []
        for i in range(len(points)):
            d = self.distanceFromOrigin(points[i])
            heapq.heappush(arr,(d,points[i]))
        while(k>0):
            distance,point = heapq.heappop(arr)
            ans.append(point)
            k-=1
        return ans