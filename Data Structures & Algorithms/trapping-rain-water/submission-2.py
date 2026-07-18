class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        #from left take the first element
        # then find the greter than left most
        # calculate teh water
        # then move needle to right
        # then again repeat the process till end
        """i=0
        j=i+1
        while(i<len(height)):
            if(height[j]<height[i]):
                j=j+1
                if(j==len(height)):
                    i = i+1
                    j = i+1
                print("current i->",i,"current j ->",j)
            else:
                w = min(height[i],height[j])*(j-i-1)
                k = i+1
                while(k<j):
                    w = w - height[k]
                    k=k+1
                    print(k)
                water+=w
                i = j
                j += 1
        return water"""
        left = list(range(len(height))) 
        right = list(range(len(height)))
        i=1
        j= len(height)-2
        left[0]= 0
        right[len(height)-1]=len(height)-1
        while(i<len(height)):
            if(height[left[i-1]]<=height[i]):
                left[i] = i
            else:
                left[i] = left[i-1]
            i+=1
        print(left)
        while(j>=0):
            if(height[right[j+1]]<=height[j]):
                right[j] = j
            else:
                right[j] = right[j+1]
            j=j-1
        print(right)
        water = 0
        for i in range(0,len(height)):
            w = min(height[left[i]],height[right[i]])-height[i]
            water+=w
        return water
        