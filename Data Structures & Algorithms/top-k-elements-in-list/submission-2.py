class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]
        
        #once or more than one == 2

        # 1 -> 1
        # 2 2 -> 2
        # 3 3 3 - > 3

        #hashmap -> values -> sort -> top K elements 

        freq_count_nums = Counter(nums)
        values_of_freq = freq_count_nums.most_common(k)
        print(values_of_freq)
        res = []
        for val, _ in values_of_freq:
            res.append(val)
        
        return res
