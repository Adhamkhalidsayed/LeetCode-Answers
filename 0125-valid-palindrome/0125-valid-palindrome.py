class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ""
        s = s.lower()
        s = re.sub(r"[^a-z0-9]","",s)

        for i in reversed(s):
            m += i
        
        return m == s