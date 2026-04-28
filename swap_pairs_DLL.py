def swap_pairs(self):
        if not self.head or not self.head.next:
            return self.head

        D=Node(0)
        D.next=self.head
        self.head.prev=D
        first=self.head
        p=D
        
        while first and first.next:
            second=first.next

            p.next=second
            second.prev=p

            first.next=second.next
            if second.next:
                second.next.prev=first

            second.next=first
            first.prev=second

            p=first
            first=first.next

        self.head=D.next
        self.head.prev=None
        return self.head    
            
            
            
    
    


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
