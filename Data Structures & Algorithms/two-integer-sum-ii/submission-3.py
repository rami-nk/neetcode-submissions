class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = defaultdict(list)

        for i in range(len(numbers)):
            if numbers[i] in lookup:
                return [lookup[numbers[i]][0], i + 1]
            lookup[target - numbers[i]].append(i + 1) 
        
