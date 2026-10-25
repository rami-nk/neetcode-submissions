class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        raw = "".join(s.split(" "))

        to_replace = []
        for i in range(len(raw)):
            char = ord(raw[i]) 
            if not ((char >= ord('a') and char <= ord('z')) or 
                   (char >= ord('A') and char <= ord('Z')) or
                   (char >= ord('0') and char <= ord('9'))):
                to_replace.append(raw[i])

        for char in to_replace:
            raw = raw.replace(char, '')

        left = 0
        right = len(raw) - 1
        for i in range(len(raw)):
            if raw[left] != raw[right]:
                return False

            left += 1
            right -= 1
            
        return True