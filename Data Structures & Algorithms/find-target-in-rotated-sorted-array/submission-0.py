class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l

        if min_index == 0:
            l = 0
            r = len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l = 0
            r = min_index - 1
        else:
            l = min_index
            r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1   