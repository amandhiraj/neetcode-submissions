class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        volume = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            volume = max(area, volume)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return volume
                
            


        