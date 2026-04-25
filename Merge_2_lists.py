
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None

        D=ListNode(0)
        curr1=list1
        curr2=list2
        temp=D

        while curr1 and curr2:
            if curr1.val<=curr2.val:
                temp.next=curr1
                temp=curr1
                curr1=curr1.next
                
            else:
                temp.next=curr2
                temp=curr2 
                curr2=curr2.next
                 
        if curr1:
            temp.next=curr1
        else:
            temp.next=curr2   
             
        head=D.next
        D.next=None

        return head           

        
        
