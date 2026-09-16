class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        chrmap = {}
        r, l = 0, 0
        while r < len(s):
            if s[r] in chrmap:
                l = max(l, chrmap[s[r]] + 1) 
            chrmap[s[r]] = r
            maxL = max(maxL, r-l+1)
            r += 1
        return maxL
            