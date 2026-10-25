class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = "".join(filter(str.isalnum, s.lower()))

        left = 0
        right = len(raw) - 1
        for i in range(len(raw)):
            if raw[left] != raw[right]:
                return False

            left += 1
            right -= 1
            
        return True