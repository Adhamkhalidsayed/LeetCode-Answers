class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        count_zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
                continue
            product *= nums[i]

        for i in nums:
            if count_zero > 1:
                ans.append(0)
            elif count_zero == 1:
                if i == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product // i)
        return ans