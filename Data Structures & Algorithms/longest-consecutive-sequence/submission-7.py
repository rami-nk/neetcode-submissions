class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        sorted_unique_nums = sorted(list((set(nums))))
        print(sorted_unique_nums)

        consecutive_len = 1
        max_len = 1
        prev = sorted_unique_nums[0]
        for i in range(1, len(sorted_unique_nums)):
            if sorted_unique_nums[i] == prev  + 1:
                consecutive_len += 1
            else:
                if consecutive_len > max_len:
                    max_len = consecutive_len
                consecutive_len = 1
            
            prev = sorted_unique_nums[i]
        
        if consecutive_len > max_len:
            max_len = consecutive_len
            

        return max_len