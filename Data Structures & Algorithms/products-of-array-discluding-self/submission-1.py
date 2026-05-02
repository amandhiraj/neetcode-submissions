class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            nums_product = 1
            for j in range(len(nums)):
                if i != j:
                    nums_product = nums_product * nums[j]
            res[i] = nums_product
        return res