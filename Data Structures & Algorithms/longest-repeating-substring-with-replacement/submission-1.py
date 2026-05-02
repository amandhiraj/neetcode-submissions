class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #AAABABB

        l = 0
        freq_count = [0] * 26
        longest_count = 0

        for r in range(len(s)):
            freq_count[ord(s[r]) - ord('A')] += 1
            while ((r - l) + 1) - max(freq_count) > k:
                freq_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest_count = max(longest_count, (r - l) + 1)
        return longest_count

 








        
        