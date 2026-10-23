class Solution:

    separator = "#"
    blank = ""
    number_joiner = ","

    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return self.blank

        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        sizes_str = self.number_joiner.join(sizes) + self.separator

        return sizes_str + self.blank.join(strs);

    def decode(self, s: str) -> List[str]:
        if s == self.blank:
            return []
        
        idx = s.index(self.separator)
        nums_str = s[:idx]
        raw_strs = s[idx+1:]

        nums = nums_str.split(self.number_joiner)
        strs = []

        idx = 0
        for i in range(len(nums)):
            length = int(nums[i])
            strs.append(raw_strs[idx:length+idx])
            idx += length

        return strs
