class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(i):
            if i == 0:
                return 0
            return (i & 1) + countOnes(i >> 1)
        
        lst = []
        for i in range(n+1):
            lst.append(countOnes(i))
        
        return lst
        

