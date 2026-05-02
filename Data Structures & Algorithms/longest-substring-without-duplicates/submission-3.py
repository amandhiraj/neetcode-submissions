class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_sub = 0
        subset = set()
        left = 0

        for right in range(len(s)):
            while s[right] in subset:
                subset.remove(s[left])
                left += 1

            subset.add(s[right])
            w = (right - left) + 1
            longest_sub = max(longest_sub, w)
        return longest_sub