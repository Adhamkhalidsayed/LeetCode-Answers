class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x = 0
        y = 1
        z = 2
        count = 0
        while z < len(nums):
            if nums[x] == 1:
                x+=1
                y+=1
                z+=1
            else:
                if nums[x] == 0:
                    nums[x] = 1
                else: nums[x] = 0
                if nums[y] == 0:
                    nums[y] = 1
                else: nums[y] = 0
                if nums[z] == 0:
                    nums[z] = 1
                else: nums[z] = 0  
                count += 1              

        if 0 in nums:
            return -1
        else: return count


