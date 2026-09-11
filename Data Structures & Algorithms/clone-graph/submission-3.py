"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
from collections import deque

class Solution:
    def getAdj(self,node: Optional['Node'])->dict[Node, List[Node]]:
        m = {}
        q = deque()
        m[node]=node.neighbors
        q.append(node)
        while(len(q)!=0):
            n = q.popleft()
            for i in range(len(n.neighbors)):
                if n.neighbors[i] not in m:
                    m[n.neighbors[i]] = n.neighbors[i].neighbors
                    q.append(n.neighbors[i])
        #for key,val in m.items():
        #    for i in range(len(val)):
        #        print("for key ",key.val,"value is ",val[i].val)
        return m
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        al = self.getAdj(node)
        hs ={}
        for key,val in al.items():
            hs[key.val] = Node(key.val)
        for key,val in al.items():
            neighbors = []
            for i in range(len(val)):
               neighbors.append(hs.get(val[i].val))
            hs.get(key.val).neighbors = neighbors
        #for key,val in m.items():
        #    for i in range(len(val)):
        #        print("for key ",key.val,"value is ",val[i].val)
        return hs.get(node.val)