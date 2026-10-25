class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_before = [0] * n
        max_before[0] = height[0]
        for i in range(1, n):
            max_before[i] = max(height[i], max_before[i-1])

        max_after = [0] * n
        max_after[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_after[i] = max(height[i], max_after[i + 1])

        water_units = 0
        for i in range(n):
            water_units += max(0, min(max_before[i], max_after[i]) - height[i])

        return water_units
