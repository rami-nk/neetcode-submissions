class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in output:
                output[k] = []

            output[k].append(s)

        return list(output.values())