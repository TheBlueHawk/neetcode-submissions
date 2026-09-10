class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        
        for c in t:
            if c in letters:
                letters[c] -=1
                if letters[c] < 0:
                    return False
            else:
                return False
        return True