class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        for s in strs:
            min_length = len(s) if len(s) < min_length else min_length

        i = 0
        while i < (min_length):
            for str in strs:
                if str[i] != strs[0][i]:
                    return str[:i]
            i += 1
            
        return s[:i]
    