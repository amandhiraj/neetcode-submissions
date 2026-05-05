import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = defaultdict(int)
        res = []
        for n in nums:
            dictt[n] = 1 + dictt.get(n, 0)
        
        sorted_items = sorted(dictt.items(), key=lambda x: x[1])
        print(sorted_items)

        for i in range(len(sorted_items) - 1, -1, -1):
            res.append(sorted_items[i][0])
            if len(res) == k:
                return res
        #[3,5,5,5,5,6,6,2,1]
        # 3 : 1
        # 5 : 4
        # 6 : 2
        # 2 : 1
        # 1 : 1
        
        #sorted by values
        # 3 : 1
        # 2 : 1
        # 1 : 1
        # 6 : 2
        # 5 : 4

        #reverse the sorted values and you get:
        # 5 : 4
        # 6 : 2
        # 3 : 1
        # 2 : 1
        # 1 : 1

