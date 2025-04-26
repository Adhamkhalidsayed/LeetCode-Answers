class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1

        while r < len(nums):
            if nums[r] > nums[l]:
                nums[l+1] = nums[r]
                l += 1
                r += 1
            else:
                r+=1
        k = l+1
        return k
