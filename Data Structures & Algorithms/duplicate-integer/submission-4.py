class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # [1,2,4,3]
        #  4
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         print(nums[i], nums[j])
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # (1,2,3,4)
        # nums[i] is in set? return True, add set continue
        set_of_numbers = set()

        for num in nums:
            if num in set_of_numbers:
                return True
            else:
                set_of_numbers.add(num)
        return False


        

         

