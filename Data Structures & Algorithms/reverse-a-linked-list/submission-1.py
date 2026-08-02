# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return None
        if(head.next is None):
            return head
        ans = ListNode()
        curr = head.next
        prev = head
        temp = curr.next
        prev.next = None
        curr.next = prev
        prev = curr
        curr = temp
        while(curr is not None):
            #print("temp->",temp,"curr->",curr,"prev->",prev)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #print(prev.val)
        return prev
