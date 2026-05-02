from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for l in s:
            if l in s_dict:
                s_dict[l] += 1
            else:
                s_dict[l] = 1
        
        for l in t:
            if l in t_dict:
                t_dict[l] += 1
            else:
                t_dict[l] = 1
        
        print(s_dict, t_dict)

        for k in s_dict.keys():
            if k not in t_dict or t_dict[k] != s_dict[k]:
                return False
        return True
        