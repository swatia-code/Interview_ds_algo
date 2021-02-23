"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        #finding search space for x value
        x_max, delta = 1, 1
        while True:
            if customfunction.f(x_max, 1) > z:
                if delta == 1: break
                delta = delta // 2
            else:
                delta = delta * 2
            x_max += delta
            
        #finding search space for y value
        y_max, delta = 1, 1
        while True:
            if customfunction.f(1, y_max) > z:
                if delta == 1: break
                delta = delta // 2
            else:
                delta = delta * 2
            y_max += delta
                
        res = list()
        x, y = 1, y_max
        while x <= x_max and y >= 1:
            val = customfunction.f(x, y)
            if val > z:
                y -= 1
            elif val < z:
                x += 1
            else:
                res.append([x, y])
                x, y = x + 1, y - 1
        
        return res
