class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dup = set()

        for num in nums:
            print(non_dup)
            if num in non_dup:
                return True
            else:
                non_dup.add(num)
        return False

