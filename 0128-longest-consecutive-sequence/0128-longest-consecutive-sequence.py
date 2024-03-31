class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_dict = {}
        max_length = 0

        for num in nums:
            if num not in num_dict:
                left = num_dict.get(num - 1, 0)
                right = num_dict.get(num + 1, 0)

                current_length = left + right + 1
                max_length = max(max_length, current_length)

                num_dict[num] = current_length
                num_dict[num - left] = current_length
                num_dict[num + right] = current_length

        return max_length
