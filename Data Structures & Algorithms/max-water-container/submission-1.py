class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_units = 0
        while l < r:
            curr_units = min(heights[r], heights[l]) * (r - l)
            if (curr_units > max_units):
                max_units = curr_units
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_units