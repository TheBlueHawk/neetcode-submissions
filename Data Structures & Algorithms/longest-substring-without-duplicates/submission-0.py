class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxL = 0
        chrs = set()
        r, l = 0, 0
        while r < len(s):
            if s[r] not in chrs:
                chrs.add(s[r])
                maxL = max(maxL, r-l+1)
                r += 1
            else:
                while s[r] in chrs:
                    chrs.remove(s[l])
                    l += 1
        return maxL
            