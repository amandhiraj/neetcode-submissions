class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueValues = set()
        for i in range(len(nums)):
            if nums[i] in uniqueValues:
                return True
            uniqueValues.add(nums[i])
        return False
