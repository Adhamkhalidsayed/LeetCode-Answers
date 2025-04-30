class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        for i in reversed(t):
            if i == s[-1]:
                s = s[:-1]
            if s == "":
                return True

        return False