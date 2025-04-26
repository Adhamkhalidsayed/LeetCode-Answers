class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        x = 0
        ans = 0

        for num in counter.keys():
            if counter [num] > x:
                x = counter[num]
                ans = num
        return ans

