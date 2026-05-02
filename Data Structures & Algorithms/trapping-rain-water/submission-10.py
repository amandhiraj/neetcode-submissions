class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        maximum_area = 0
        left , right = 0, len(height) - 1

        max_l, max_r = height[left], height[right]

        while left < right:
            if max_l < max_r:
                left += 1
                max_l = max(max_l, height[left])
                maximum_area += max_l - height[left]
            else:
                right -= 1
                max_r = max(max_r, height[right]) 
                maximum_area += max_r - height[right]  
        return maximum_area


            


