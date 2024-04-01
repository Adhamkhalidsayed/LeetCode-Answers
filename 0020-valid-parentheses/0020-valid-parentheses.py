class Solution:
    def isValid(self, s: str) -> bool:
        checkP = {")":"(","}":"{","]":"["}
        stack = []
        
        for i in s:
            if i not in checkP:
                stack.append(i)
                continue
            if stack and (stack[-1] == checkP[i]):
                stack.pop()
            else:
                return False
        return not stack
                    