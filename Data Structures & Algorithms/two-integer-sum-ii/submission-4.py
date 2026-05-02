class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


            # 1,2,3,4
            # i.    j 

            # s = 0 

            # 5 == s:
            # j down
            # 4 == s
            # j  down:
            # 3 == s
            # i and j


            # if i == j 
            # i += 1 
            # j = len() - 1


            s = 0
            left, right = 0, len(numbers) - 1

            while left < right:
                s = numbers[left] + numbers[right]
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return[left + 1,  right + 1]
            return s
                


