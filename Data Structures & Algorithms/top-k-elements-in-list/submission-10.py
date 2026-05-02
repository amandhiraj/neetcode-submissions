import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = Counter(nums) 
        # heap = []
        # for key, val in freq.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (val, key))
        #     else:
        #         heapq.heappushpop(heap, (val, key))
        # return [h[1] for h in heap]

        freq = Counter(nums)
        bucket = [0] * (len(nums) + 1)

        for key, val in freq.items():
            if bucket[val] == 0:
                bucket[val] = [key]
            else:
                bucket[val].append(key)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            if len(res) < k and bucket[i] != 0:
                res.extend(bucket[i])
        
        return res
        