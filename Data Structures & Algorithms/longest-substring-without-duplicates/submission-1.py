class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        sub_strings = set()
        longest_seq = 0

        for r in range(len(s)):
            while s[r] in sub_strings:
                sub_strings.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            longest_seq = max(w, longest_seq)
            sub_strings.add(s[r])
        return longest_seq




            