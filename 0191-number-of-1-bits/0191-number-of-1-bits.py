class Solution:
    def hammingWeight(self, n: int) -> int:
        numOfOnes = 0
        while n:
            if n % 2 == 1:
                numOfOnes += 1
            n = n // 2
        return numOfOnes