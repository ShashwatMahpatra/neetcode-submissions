from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        
        while l < r:
            # Step 1: Calculate area
            area = min(heights[l], heights[r]) * (r - l)
            
            # Step 2: Update max area
            res = max(res, area)
            
            # Step 3: Move pointer
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        # ✅ Return after loop completes
        return res
