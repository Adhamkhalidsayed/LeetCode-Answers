class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i+1 < len(nums):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                break
            else:
                i+=1
        return nums[i]