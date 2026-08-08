# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head is None):
            return None
        length = 0
        cur = head
        n = k
        while(n>0):
            cur = cur.next
            n-=1
            if(cur is None and n>0):
                return head
        curr = head
        prev = None
        n = k
        while(curr and n>0):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n-=1
        n = k
        head.next = self.reverseKGroup(curr,n)
        return prev
