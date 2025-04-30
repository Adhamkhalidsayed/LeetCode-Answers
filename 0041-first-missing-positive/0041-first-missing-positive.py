class Solution:
    def firstMissingPositive(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0

        print(nums)

        absolute = 0
        for j in range(len(nums)):
            absolute = abs(nums[j])
            if 1 <= absolute <= len(nums):
                if nums[absolute -1] > 0:
                    nums[absolute - 1] = -nums[absolute - 1]
                elif nums[absolute - 1] == 0:
                    nums[absolute - 1] = -(len(nums) + 1)

        print(nums)
        for k in range(len(nums)):
            if nums[k] >= 0:
                return k + 1
        return len(nums) + 1


        