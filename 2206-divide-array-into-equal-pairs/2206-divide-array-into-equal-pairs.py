class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dir = Counter(nums)
        for i in dir:
            if dir[i] % 2 == 0:
                continue
            else: return False
        return True