class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product= 1
    
        if nums.count(0) < len(nums): 
            for num in nums:
                if num != 0:
                    product *= num

        if nums.count(0) >= 2:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            return [product if num == 0 else 0 for num in nums]
        else:
            return [product // num for num in nums]
        
        
        
