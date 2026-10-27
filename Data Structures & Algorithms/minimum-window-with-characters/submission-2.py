class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = defaultdict(int)

        for char in t:
            count[char] += 1

        missing = len(t)
        left = 0
        best_start = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            if count[char] > 0:
                missing -= 1

            count[char] -= 1

            # Try to shrink while the window is valid
            while missing == 0:
                window_length = right - left + 1

                if window_length < best_length:
                    best_start = left
                    best_length = window_length

                left_char = s[left]
                count[left_char] += 1

                if count[left_char] > 0:
                    missing += 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]