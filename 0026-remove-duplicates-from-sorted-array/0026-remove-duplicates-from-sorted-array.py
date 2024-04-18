class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0

        while i < len(nums) and i+1 < len(nums):
            if nums[i+1] != nums[i]:
                i+=1
            else:
                del nums[i]
        


            