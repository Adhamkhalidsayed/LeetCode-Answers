class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        j = k+1

        while j < len(nums):
            if nums[k] == nums[j]:
                j +=1
            else:
                nums[k+1] = nums[j]
                k +=1
        k +=1
        return k