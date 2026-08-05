# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = ListNode()
        head = sum
        while(l1 and l2):
            temp = ListNode()
            sum.next = temp
            sum = sum.next
            sum.val = (carry + l1.val + l2.val)%10
            carry = (carry + l1.val + l2.val)//10
            l1 = l1.next
            l2 = l2.next
        while(l1 is None and l2 is not None):
            temp = ListNode()
            sum.next = temp
            sum = sum.next
            sum.val = (carry +  l2.val)%10
            carry = (carry +  l2.val)//10
            l2 = l2.next
        while(l2 is None and l1 is not None):
            temp = ListNode()
            sum.next = temp
            sum = sum.next
            sum.val = (carry +  l1.val)%10
            carry = (carry +  l1.val)//10
            l1 = l1.next
        #print("sum value",sum.val)
        if(carry!=0):
            temp = ListNode()
            sum.next = temp
            sum = sum.next
            sum.val = 1
            sum.next = None
        return head.next