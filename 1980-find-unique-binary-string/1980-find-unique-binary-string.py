class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        zeros = "0" * len(nums[0])
        ones = "1" * len(nums[0])
        
        if "0" * len(nums[0]) not in nums:
            return "0" * len(nums[0])
        if ones not in nums:
            return ones
        else:
            for i in range(int(nums[-1])+1):
                n_bin= bin(i)[2:]
                n_bin = n_bin.zfill(len(nums[-1]))
                if n_bin not in nums:
                    return n_bin
