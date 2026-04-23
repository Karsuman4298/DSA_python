def partition_list(self,x):
        if self.head is None:
            return None
        curr=self.head
        d1=Node(0)
        d2=Node(0)
        prev1=d1
        prev2=d2
        while curr:
            if curr.value <x:
                prev1.next=curr
                prev1=curr
                curr=curr.next
                
                
            elif curr.value >= x:
                prev2.next=curr
                prev2=curr
                curr=curr.next
                
        prev1.next=d2.next
        prev1=None
        self.head=d1.next
        d2.next=None
        prev2.next=None
        
