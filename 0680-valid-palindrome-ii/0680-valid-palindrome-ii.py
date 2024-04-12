class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                left = s[i:~i]
                right = s[i+1:len(s)-i]
                return left == left[::-1] or right == right[::-1]
        return True