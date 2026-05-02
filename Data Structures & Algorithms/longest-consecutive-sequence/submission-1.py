class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        longest_cons_num = 0
        for num in nums:
            if (num - 1) not in nums_set:
                length_curr_seq = 1
                while num + length_curr_seq in nums_set:
                    length_curr_seq += 1
                longest_cons_num = max(longest_cons_num, length_curr_seq)
        
        return longest_cons_num
                




        