class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        mem = 0
        counter = 0
        while i < len(nums):
            if nums[i] == 0:
                counter += 1
                mem += counter
            else:
                counter = 0
            i += 1
        return mem