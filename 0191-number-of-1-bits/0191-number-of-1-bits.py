class Solution:
    def hammingWeight(self, n: int) -> int:
        numOfOnes = 0
        while n > 0:
            x = n // 2
            y = n / 2
            
            if x != y:
                numOfOnes += 1
            n = x
        
        return numOfOnes