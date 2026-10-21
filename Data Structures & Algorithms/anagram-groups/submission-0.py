class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_original = strs.copy()

        for i in range(0, len(strs)):
            s = "".join(sorted(strs[i]))
            strs[i] = s

        output = {}
        for i in range(0, len(strs)):
            s = strs[i]
            if s not in output:
                output[s] = []

            output[s].append(strs_original[i])

        return list(output.values())

        