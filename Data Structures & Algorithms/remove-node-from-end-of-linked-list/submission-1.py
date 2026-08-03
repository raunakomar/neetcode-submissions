# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        k = n
        while(k>0 and fast is not None):
            fast = fast.next
            k-=1
        if(fast is None and k==0):
            return slow.next
        if(fast is None and k!=0):
            return None
        while(fast.next is not None):
            slow = slow.next
            fast = fast.next
        print("fast ", fast.val," slow" , slow.val)
        temp = slow.next.next
        slow.next = temp
        return head

        