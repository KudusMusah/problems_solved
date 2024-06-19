import math 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))

        while l <= r:
            curr = l**2 + r**2
            if curr < c:
                l += 1
            elif curr > c:
                r -= 1
            else:
                return True
        return False
        