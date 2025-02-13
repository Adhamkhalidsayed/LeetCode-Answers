class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operation = 0
        nums.sort()
        while nums[0] < k:
            nums.pop(0)
            operation += 1

        return operation
             