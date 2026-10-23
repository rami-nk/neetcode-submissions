class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        sizes_str = ",".join(sizes) + "#"

        return sizes_str + "".join(strs);

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        idx = s.index("#")
        nums_str = s[:idx]
        raw_strs = s[idx+1:]

        print(raw_strs)
        print(nums_str)

        nums = nums_str.split(",")
        strs = []

        idx = 0
        for i in range(len(nums)):
            length = int(nums[i])
            print(idx)
            print(length)
            print(raw_strs[idx:length])
            strs.append(raw_strs[idx:length+idx])
            idx += length

        return strs
