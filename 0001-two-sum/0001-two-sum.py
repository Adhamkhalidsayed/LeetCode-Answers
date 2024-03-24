class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            n = nums[i]
            complement = target - n
            if complement in seen:
                return [i,seen[complement]]
            seen[n]=i
            i +=1