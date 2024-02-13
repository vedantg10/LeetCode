class Solution:
    def myPow(self, x: float, n: int) -> float:
        if int(n) == 0:
            return 1
        if n<0:
            n = abs(n)
            x = 1/x
        if (n%2 == 0):
            return self.myPow(x*x, n//2)
        else:
            return x * (self.myPow(x,n-1)) 