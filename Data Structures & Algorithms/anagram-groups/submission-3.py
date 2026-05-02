class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        dict = {
            act: [act, cat],
            pots: [pots, stop, tops]
            hat: [hat]
        
        }

        checkAnagram(key, word)
            - check if its anagram of key and current word
            - if its anagram i want to return true otherwise false

        main function:
            - check if its anagram
                - if anagram and exists in dict, add it to key as value
                - else add the word to dict with as key =word, value=[word]
            - return the values at the end
        
        """
        anagrams = {}
        for word in strs:
            sorted_w = ''.join(sorted(word))  
            if sorted_w in anagrams:
                anagrams[sorted_w].append(word)
            else:
                anagrams[sorted_w] = [word]
        return [val for val in anagrams.values()]
                






