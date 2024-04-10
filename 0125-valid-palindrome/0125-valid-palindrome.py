class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(i for i in s if i.isalnum()).lower()
        
        return str(x) == str(x)[::-1]