# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):
            return 1
        if(n < 0):
            ans = (1/x)*self.myPow(x, n+1)
        else:
            ans = x*self.myPow(x, n-1)
        return ans