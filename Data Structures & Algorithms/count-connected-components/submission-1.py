from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ar = []
        q = deque()
        for i in range(n):
            ar.append([])
        for i in range(len(edges)):
            ar[edges[i][0]].append(edges[i][1])
            ar[edges[i][1]].append(edges[i][0])
        for i in range(len(ar)):
            for j in range(len(ar[i])):
                print("for ",i ,"and", j, ar[i][j])
        component = 0
        visited = [0]*(n)
        for j in range(len(visited)):
            if(visited[j]==0):
                print("visited ",j ," is false")
                component+=1
                q.append(j)
                visited[j] = 1
                while(len(q)>0):
                    node = q.popleft()
                    for i in range(len(ar[node])):
                        #print("i in ",i,node)
                        if(visited[ar[node][i]]==0):
                            visited[ar[node][i]]=1
                            q.append(ar[node][i])
        return component
