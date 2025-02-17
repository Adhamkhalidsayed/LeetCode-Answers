class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m = re.split("\s", s)
        x = -1
        while True:
            if m[x] == '':
                x -= 1
            else:
                break
        return len(m[x])