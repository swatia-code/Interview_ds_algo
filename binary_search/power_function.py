class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow_helper(x, n):
            if n == 0:
                return 1
            
            half_val = pow_helper(x, n // 2)
            if n & 1:
                return half_val * half_val * x
            else:
                return half_val * half_val
            
        if n < 0:
            x = 1 / x
            n = -1 * n
            
        return pow_helper(x, n)
