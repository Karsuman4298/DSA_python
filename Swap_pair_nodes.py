
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        D=ListNode(0,head)
        prev=D
        first=D.next

        
        while first and first.next:
            second=first.next

            first.next=second.next
            second.next=first
            prev.next=second

            prev=first
            first=first.next

        head=D.next
        return head        

        
