class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i, v in enumerate(nums):
            comp = target - nums[i]
            if comp in dictt:
                return [dictt[comp], i]
            else:
                dictt[v] = i
        return []
        