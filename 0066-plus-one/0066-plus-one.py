class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]

        x = list(str(int(''.join(s)) + 1))

        x = [int(i) for i in x]
        
        return x