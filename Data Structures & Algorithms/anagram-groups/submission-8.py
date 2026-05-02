class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            #   [["hat"],["act", "cat"],["stop", "pots", "tops"]]
            #     {
            #         act:  [act, cat]
            #         opst:  [pots, tops, stop]
            #         aht: [hat]
            #     }
            # [[act, cat], [pots, tops, stop], [hat]]

            dictt = {}
            for s in strs:
                sorted_s = ''.join(sorted(s))
                if sorted_s in dictt:
                    dictt[sorted_s].append(s)
                else:
                    dictt[sorted_s] = [s]
            return list(dictt.values())
            



