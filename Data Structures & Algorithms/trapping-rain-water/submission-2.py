class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_before = [0] * n
        curr_max = max_before[0]
        for i in range(0, n):
            if height[i] > curr_max:
                curr_max = height[i]
            max_before[i] = curr_max


        max_after = [0] * n
        curr_max = max_after[n - 1]
        for i in range(n - 1, -1, -1):
            if height[i] > curr_max:
                curr_max = height[i]
            max_after[i] = curr_max

        water_units = 0
        for i in range(n):
            water_units += max(0, min(max_before[i], max_after[i]) - height[i])

        return water_units
