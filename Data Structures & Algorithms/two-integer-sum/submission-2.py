class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = {}
        res = []
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in comp_dict:
                return [min(idx, comp_dict[comp]), max(idx, comp_dict[comp])]
            comp_dict[num] = idx
        return [] 
        