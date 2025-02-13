import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_o = 0

        heapq.heapify(nums)

        while len(nums) >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k and y >= k:
                nums.append(x)
                nums.append(y)
                break
            else:
                nums.append(min(x, y) * 2 + max(x, y))
                num_o += 1

        return num_o