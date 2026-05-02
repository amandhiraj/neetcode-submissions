class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Input: nums = [3,4,5,6], target = 7
        # Output: [0,1]

        # 7 return 3+ 4 = 7 [ 0, 1]

        complement_numbers = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complement_numbers:
                return [complement_numbers[comp], i]
            complement_numbers[nums[i]] = i
        return []
            









        
        

        