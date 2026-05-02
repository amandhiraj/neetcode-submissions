class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i < j:
            summed_val = numbers[i] + numbers[j]
            if summed_val == target:
                return [i + 1, j + 1]
            elif summed_val < target:
                i += 1
            else:
                j -= 1
        return []
        