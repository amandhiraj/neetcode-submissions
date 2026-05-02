class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0

        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1] = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
            else:
                res.append(intervals[i])
            i += 1

        print(intervals[-1])
        res.append(intervals[-1])
        return res        