class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            uniques.add(s[r])
            res = max(res, r - l + 1)
        return res