def binary_to_decimal(self):
  curr=self.head
  num=0
  while curr:
    num=num*2 + curr.value
    curr=curr.next

  return num


#OUTPUT:
# linked list:
# 1 -> 1 -> 0
# returned: 6
