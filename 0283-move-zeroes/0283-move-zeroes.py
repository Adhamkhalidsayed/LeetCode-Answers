class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        countZero = 0
        while i < len(nums):
            if nums[i] != 0:
                i+=1
            else:
                del nums[i]
                countZero +=1
        for i in range(countZero):
            nums.append(0)