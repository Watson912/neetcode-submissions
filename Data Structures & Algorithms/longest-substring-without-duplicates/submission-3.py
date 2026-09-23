class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l= 0
        res = 0

        if s == "":
            return 0
        elif len(s) == 1:
            return 1

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res