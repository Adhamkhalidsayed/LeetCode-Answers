class Solution:
    def reverseBits(self, n: int) -> int:
        
        x = 0
        num = 0
        for i in range(31,-1,-1):
            x = n & 1
            n = n >> 1
            if x == 1:
                num += x * (2**i)
        
        return num
