class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            first_largest_value = heapq.heappop(stones)
            second_largest_value = heapq.heappop(stones)

            if first_largest_value < second_largest_value:
                diff = first_largest_value - second_largest_value
                heapq.heappush(stones, diff)
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0





        