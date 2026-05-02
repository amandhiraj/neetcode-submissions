class Solution:
    def isPalindrome(self, s: str) -> bool:

        # S(a-Z)

        #cattac
        # c - c
        # a - a
        # t - t

        #"Was it a car or a cat I saw?"

        #1) !isAlphanumeric -> move left or right
        #2) lowercase(input)
        #3) if right and left == move inwards

        left, right = 0, len(s) - 1

        while left < right:
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].isalnum():
                left += 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
                







