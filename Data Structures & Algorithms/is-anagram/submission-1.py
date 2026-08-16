class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}

        for i in s:
            if i in chars:
                chars[i] = chars[i] + 1
            else: 
                chars[i] = 1

        for i in t:
            if i in chars:
                chars[i] = chars[i] - 1
            else: 
                return False

        for key,val in chars.items():

            if chars[key] != 0:
                return False
        return True
            
        