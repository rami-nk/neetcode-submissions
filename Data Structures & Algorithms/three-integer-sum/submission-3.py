class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i, fixed in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -fixed:
                    triplets.append([nums[l], nums[r], fixed])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > -fixed:
                    r -= 1
                else:
                    l += 1
        
        return triplets
