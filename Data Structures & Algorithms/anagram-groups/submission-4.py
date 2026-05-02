class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_w = ''.join(sorted(word))  
            if sorted_w in anagrams:
                anagrams[sorted_w].append(word)
            else:
                anagrams[sorted_w] = [word]
        return [val for val in anagrams.values()]
                






