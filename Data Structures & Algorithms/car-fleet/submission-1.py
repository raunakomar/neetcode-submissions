class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(key=lambda row: row[0])
        
        time = []
        for i in range(len(cars)):
            time.append((target-cars[i][0])/cars[i][1])
        for i in range(len(time)):
            if(len(stk)==0):
                stk.append(time[i])
            elif(stk[-1]<=time[i]):
                while(len(stk)>0 and stk[-1]<=time[i]):
                    stk.pop()
                stk.append(time[i])
            else:
                stk.append(time[i])
        
        return (len(stk))