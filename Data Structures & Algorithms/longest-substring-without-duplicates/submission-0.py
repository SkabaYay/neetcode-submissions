class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChar = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in seenChar:
                l = max(seenChar[s[r]] + 1, l)
            seenChar[s[r]] = r
            res = max(res, r - l + 1)
        return res