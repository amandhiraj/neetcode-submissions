class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = {}
        res = []
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in comp_dict:
                return [comp_dict[comp], idx]
            comp_dict[num] = idx
        return [] 
        