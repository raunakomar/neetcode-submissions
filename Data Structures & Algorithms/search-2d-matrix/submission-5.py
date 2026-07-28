class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix))*(len(matrix[0])) -1
        row = len(matrix)
        col = len(matrix[0])
        while l<=r:
            mid = int((l+r)/2)
            print("l->",l,"r->",r,"mid->",mid)
            if(matrix[int(mid/col)][int(mid%col)]<target):
                l = mid+1
            elif((matrix[int(mid/col)][int(mid%col)]>target)):
                r = mid-1
            else:
                return True
        return False       