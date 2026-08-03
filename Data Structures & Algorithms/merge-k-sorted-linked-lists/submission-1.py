# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #prepare a new list
        #prepare a new head 
        #keep on adding to this head
        #retrun head
        #have 2 pointers h1 and h2
        #while both are not null 
        #till then merge
        #after that merge non null
        curr = None
        h1 = list1
        h2 = list2
        if(h1 is None):
            return h2
        if(h2 is None):
            return h1
        if(h1.val<=h2.val):
            curr = h1
            h1 = h1.next
        elif(h1.val>h2.val):
            curr = h2
            h2 = h2.next
        head = curr
        #print(head.val)
        #print("starting h1 is ",h1.val,"h2 is ",h2.val)
        while(h1 is not None and h2 is not None):
            if(h1.val<h2.val):
                #print("h1 is less than h2")
                curr.next = h1
                curr = curr.next
                #print("curr is ",curr.val,"h1 is ",h1.val)
                h1 = h1.next
            else:
                #print("h2 is less than h1")
                curr.next = h2
                curr = curr.next
                #print("curr is ",curr.val,"h2 is ",h2.val)
                h2 = h2.next
        if(h1 is None):
            curr.next = h2
        if(h2 is None):
            curr.next = h1
        return head  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists)==0):
            return None
        if(len(lists)==1):
            return lists[0]
        l1 = lists[0]
        l2 = lists[1]
        ml = self.mergeTwoLists(l1,l2)
        h1 = ml
        curr = 2
        while(curr<len(lists)):
            h1 = self.mergeTwoLists(h1,lists[curr])
            curr+=1
        return h1
        