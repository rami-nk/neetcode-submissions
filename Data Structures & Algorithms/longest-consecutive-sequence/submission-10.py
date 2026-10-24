class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)

        consecutive_len = 1
        max_len = consecutive_len
        prev = sorted_nums[0]
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == prev:
                continue
            if sorted_nums[i] == prev  + 1:
                consecutive_len += 1
            else:
                if consecutive_len > max_len:
                    max_len = consecutive_len
                consecutive_len = 1
            
            prev = sorted_nums[i]
        
        if consecutive_len > max_len:
            max_len = consecutive_len
            
        return max_len