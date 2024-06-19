from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        max_ = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)
            max_ = max(max_, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        
        return max_