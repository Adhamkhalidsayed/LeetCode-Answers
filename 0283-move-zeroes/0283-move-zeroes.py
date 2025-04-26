class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 1
        if nums == [] or 0 not in nums or len(nums) == 1:
            return
        
        while r < len(nums):
                if nums[l] == 0 and nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                elif nums[l] == 0 and nums[r] == 0:
                    r += 1
                elif nums[l] != 0 and nums[r] == 0:
                    l += 1
                    r += 1
                else:
                    l += 1
                    r += 1

        