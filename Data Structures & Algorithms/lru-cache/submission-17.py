class ListNode:
     def __init__(self, key=0 ,val=0, next=None,prev =None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
         

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFirst(self,n:ListNode) -> None:
       ch = self.head.next 
       n.next = ch
       n.prev = self.head
       self.head.next = n
       ch.prev = n

    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key: int) -> int:
        if(key in self.map):
            self.removeNode(self.map[key])
            self.insertFirst(self.map[key])
            return self.map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.map):
            self.removeNode(self.map[key])
        self.map[key] = ListNode(key,value)
        self.insertFirst(self.map[key])
        if len(self.map)>self.capacity:
            n = self.tail.prev
            self.removeNode(n)
            del self.map[n.key]

