def partition_list(self, x):
        if self.head is None:
            return None
            
        D1=Node(0)
        D2=Node(0)
        curr=self.head
        prev1=D1
        prev2=D2
        
        while curr:
            nxt = curr.next   
            curr.next = None
            curr.prev = None
            if curr.value<x:
                prev1.next=curr
                curr.prev=prev1
                prev1=curr
            
                
            else:
            
                prev2.next=curr
                curr.prev=prev2
                prev2=curr
                
            curr=nxt    
                
                 
        prev1.next=D2.next
        if D2.next:
            D2.next.prev=prev1

        self.head=D1.next
        if self.head:
            self.head.prev=None    

        return self.head    


"""
sumankar@Mac dsa %  python3 test.py

Test Case 1: Partition around 5
BEFORE: 3
8
5
10
2
1
AFTER:  3
2
1
8
5
10

Test Case 2: All nodes less than x
BEFORE: 1
2
3
AFTER:  1
2
3

Test Case 3: All nodes greater than x
BEFORE: 6
7
8
AFTER:  6
7
8

Test Case 4: Empty list
BEFORE: AFTER:  
Test Case 5: Single node
BEFORE: 1
AFTER:  1 """
