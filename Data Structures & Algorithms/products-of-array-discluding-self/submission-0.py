class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_occ = 0
        for num in nums:
            if num==0:
                total_prod = total_prod
                zero_occ+=1
            else:
                total_prod *= num
        print(total_prod)
        result = []
        if(zero_occ==0):
            for num in nums:
                result.append(int(total_prod/num))
        elif(zero_occ==1):
            for num in nums:
                if(num!=0):
                    result.append(0)
                else:
                    result.append(total_prod)
        else:
            for num in nums:
                result.append(0)
        return result
                
        