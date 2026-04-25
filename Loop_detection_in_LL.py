def has_loop(self):
        slow=self.head
        fast=self.head
        
        while fast is not None and fast.next is not None:
            
            fast=fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
