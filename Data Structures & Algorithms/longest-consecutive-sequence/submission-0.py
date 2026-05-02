class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        # [2,3,4,5,10,20]
        # set (2) -> check if element is a starting seq of set by curr - 1
        # if it is then check every value after that element and see if its in the set
        # then check which seq is the highest

        longCons = set(nums)
        totalCons = 0
        
        print(longCons)
        for i in nums:
            print(f'Current value = {i} | -1 = {i - 1} | +1 = {i+1} | {i - 1 in longCons} or {i + 1 in longCons}')
            if i - 1 not in longCons:
                lengthOfSeq = 0
                #means its the start of the john
                while (i + lengthOfSeq) in longCons:
                    lengthOfSeq += 1
                totalCons = max(lengthOfSeq, totalCons) 

        return totalCons 





        