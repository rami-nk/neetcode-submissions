class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) - 1
        freqs_s1 = [0] * 26
        freqs_s2 = [0] * 26

        for i in range(len(s1)):
            freqs_s1[ord(s1[i]) - ord('a')] += 1

        for i in range(l, r + 1):
            freqs_s2[ord(s2[i]) - ord('a')] += 1

        while r < len(s2):
            if freqs_s1 == freqs_s2:
                return True
            freqs_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if (r < len(s2)):
                freqs_s2[ord(s2[r]) - ord('a')] += 1
        return False