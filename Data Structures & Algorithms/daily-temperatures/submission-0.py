class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # (temp, index)
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _ , stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temp, i))
        return result

        # temp = 28, i = 6
        # stack = [(40, 5), (28, 6)]
        # current value pair = 
        # res = [1, 4, 1, 2, 1, 0, 0]


        