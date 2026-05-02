class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        # If s1 is longer than s2, a permutation of s1 can't fit in s2
        if n1 > n2:
            return False
        
        # Frequency count for s1
        s1_counts = [0] * 26
        # Frequency count for the current window in s2
        window_counts = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
        
        # If the initial window matches, return True
        if window_counts == s1_counts:
            return True

        # Slide the window across s2
        for i in range(n1, n2):
            # Add the new character to the window
            window_counts[ord(s2[i]) - ord('a')] += 1
            # Remove the character that just slid out of the window
            window_counts[ord(s2[i - n1]) - ord('a')] -= 1

            # Check if the current window's frequency matches s1's frequency
            if window_counts == s1_counts:
                return True
        
        return False
