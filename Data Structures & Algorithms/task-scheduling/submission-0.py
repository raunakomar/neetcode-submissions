import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        
        for i in range(len(tasks)):
            mp[tasks[i]]= mp.get(tasks[i], 0) + 1
        i = 0
        arr = [0] * len(mp)
        for key,val in mp.items():
            print("i",i)
            arr[i] = -1*val
            i+=1
        heapq.heapify(arr)
        que = deque()
        for i in range(len(arr)):
            print(arr[i])
        timer = 0
        while(que or arr):
            timer+=1
            if arr:
                data = -heapq.heappop(arr)
                if data > 1:
                    que.append((data - 1, timer + n))

            if que:
                freq, time = que[0]
                if timer >= time:
                    heapq.heappush(arr, -freq)
                    que.popleft()
        
        
        return timer