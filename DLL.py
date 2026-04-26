class Node:
    def __init__(self,value):
        self.prev=None
        self.value=value
        self.next=None
        
        
class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next  

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node

        self.length+=1      

    def pop(self):
        if self.length==0:
            return None
        
        temp=self.tail

        if self.length==1:
            self.head=None
            self.tail=None

        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None    
            self.length-=1

        return temp   
    
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.head=new_nodes
            self.tail=new_node

        new_node.next=self.head
        self.head.prev=new_node
        self.head=self.head.prev    
        self.length+=1

    def pop_first(self):
    
        if self.length==0:
            return None
        
        temp=self.head

        if self.length==1:
            self.head=None
            self.tail=None

        else:
            self.head=temp.next
            temp.next=None
            self.head.prev=None
        self.length-=1
        return temp    
    
    def get(self,index):
        if index<0  or index>=self.length:
            return None
        
        if index<self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next

        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp    


    def set_value(self,index,value):
        if index<0  or index>=self.length:
            return None
        
        if index<self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next

        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev

        temp.value=value
 

    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    

    def remove(self,index):
        if index<0 or index >=self.length:
            return None
            
        if index ==0:
            return self.pop_first()
            
        if index== self.length-1:
            return self.pop()

        before=self.get(index-1)
        temp=self.get(index)
        after=temp.next

        before.next=after
        after.prev=before
        temp.prev=None
        temp.next=None
        self.length-=1    
        return temp





my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""

