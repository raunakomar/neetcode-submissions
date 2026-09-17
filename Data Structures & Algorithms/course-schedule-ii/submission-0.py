class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ar = [[] for i in range(numCourses)]
        inDegree = [0]*numCourses
        for i in range(len(prerequisites)):
            ar[prerequisites[i][0]].append(prerequisites[i][1])
            ar[prerequisites[i][1]].append(prerequisites[i][0])
            inDegree[prerequisites[i][0]]+=1
        q = deque()
        ans = []
        for i in range(len(inDegree)):
            if(inDegree[i]==0):
                q.append(i)
        if(len(q)==0):
            return []
        while(q):
            n = q.popleft()
            #print("n is ",n)
            ans.append(n)
            for i in range(len(ar[n])):
                #print("ar[n][i] is",ar[n][i] ," and inDegree[ar[n][i]] is",inDegree[ar[n][i]])
                if(inDegree[ar[n][i]]>0):
                    inDegree[ar[n][i]]-=1
                    if(inDegree[ar[n][i]]==0):
                        q.append(ar[n][i])
                        #print("appended ",ar[n][i])
        if(len(ans)==numCourses):
            return ans
        return []