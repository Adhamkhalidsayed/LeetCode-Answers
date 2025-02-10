class Solution:
    def clearDigits(self, s: str) -> str:
        new_s = ""

        for i in range(len(s)):
            if s[i].isdigit():
                if new_s != "":
                    new_s = new_s[:-1]
            else:
                new_s += s[i]
        return new_s