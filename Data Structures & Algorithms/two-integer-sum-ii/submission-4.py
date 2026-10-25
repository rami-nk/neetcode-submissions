class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(numbers)):
            if numbers[i] in lookup:
                return [lookup[numbers[i]], i + 1]
            lookup[target - numbers[i]] = i + 1 
        
