
def in_common_brute_force(list1,list2): # O(N^2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                return True
    return False        


def in_common_efficient(list1,list2): # O(2N)
    my_dict={}
    for i in range(len(list1)):
        my_dict[list1[i]]=True

    for j in range(len(list2)):
        if list2[j] in my_dict:
            return True

    return False        

                  


l1=[1,2,5]
l2=[1,6,0]

print(in_common_brute_force(l1,l2))
print(in_common_efficient(l1,l2))

"""

OUTPUT:
True
True

"""
