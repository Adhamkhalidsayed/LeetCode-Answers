class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = " ".join(s.split())
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                break
            else:
                c += 1
        return c