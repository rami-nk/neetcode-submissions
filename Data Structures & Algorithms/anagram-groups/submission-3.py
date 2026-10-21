class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in range(0, len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in output:
                output[s] = []

            output[s].append(strs[i])

        return list(output.values())

        