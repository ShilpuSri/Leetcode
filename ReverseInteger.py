class Solution:
    def reverse(self, x: int) -> int:
        if x >= pow(-2, 31) and x <= (pow(2,31) - 1):
            rev=0
            orig=x
            if orig < 0:
                x=x+(2*(-x))
            while x > 0:
                rem=x%10
                rev=rev*10+rem
                x=int(x/10)
            if orig < 0:
                rev=rev-(2*rev)
            if rev >= pow(-2, 31) and rev <= (pow(2,31) - 1):
                return rev
            else:
                return 0
            