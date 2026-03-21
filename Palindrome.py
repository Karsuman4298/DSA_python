class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        rev_num=0
        temp=x

        while temp>0:
            rev_num=rev_num*10 + (temp%10)
            temp//=10

        return x==rev_num      
        
