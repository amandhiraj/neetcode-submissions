class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # [1,2,4,3]

        #  4

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(nums[i], nums[j])
                if nums[i] == nums[j]:
                    return True
        return False

         

