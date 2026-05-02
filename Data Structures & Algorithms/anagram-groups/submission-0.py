class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_anagrams = defaultdict(list)

        for word in strs:
            ascii_count = [0] * 26
            for char in word:
                ascii_count[ord(char) - ord('a')] += 1
            grouped_anagrams[tuple(ascii_count)].append(word)
        return grouped_anagrams.values()
        