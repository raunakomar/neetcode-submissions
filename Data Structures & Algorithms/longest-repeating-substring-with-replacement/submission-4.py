class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #max_length = 0
        #i = 0
        #n = k
        #curr = 0
        #start from index 0
        #have it last seen
        #move i
        #if different then check n
        #if n >0 then increase length and move i
        #else check max_length and curr_length
        #and reset n and repeat till end
        #while(i<len(s)):
        #    if(curr == 0):
        #        running = s[i]
        #        curr+=1
        #        i+=1
        #    elif(s[i]==running):
        #        curr+=1
        #        i+=1
        #    else:
        #        if(n>0):
        #            curr+=1
        #            i+=1
        #            n-=1
        #        else:
        #            max_length = max(max_length,curr)
        #            curr=0
        #            n=k
        #return max(max_length,curr)
        count = {}
        max_length = 0
        l = 0
        for r in range(0,len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            while((r-l+1)-max(count.values())>k):
                count[s[l]]-=1
                l+=1
            max_length = max(max_length,r-l+1)
        return max_length


            