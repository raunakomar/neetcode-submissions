class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #not optimized but trying
        max_area = 0
        for i in range(len(heights)):
            j = i
            height = heights[j]
            while j < len(heights):
                area = 0
                if(i==j):
                    area = heights[i]
                    max_area = max(area,max_area)
                    j+=1
                else:
                    width = j-i+1
                    height = min(height,heights[j])
                    area = width*height
                    max_area = max(area,max_area)
                    j+=1
        return max_area