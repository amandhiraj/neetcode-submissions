class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {}
        # for word in strs:
        #     sorted_w = ''.join(sorted(word))  
        #     if sorted_w in anagrams:
        #         anagrams[sorted_w].append(word)
        #     else:
        #         anagrams[sorted_w] = [word]
        # return [val for val in anagrams.values()]
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        print(res)
        return list(res.values())
                






