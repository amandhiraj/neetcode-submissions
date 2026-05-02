import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = defaultdict(int)
        res = []
        for n in nums:
            if n in dictt:
                dictt[n] += 1
            else:
                dictt[n] = 1
        
        sorted_items = sorted(dictt.items(), key=lambda x: x[1])

        for i in range(len(sorted_items) - 1, -1, -1):
            if len(res) < k:
                res.append(sorted_items[i][0])

        return res
