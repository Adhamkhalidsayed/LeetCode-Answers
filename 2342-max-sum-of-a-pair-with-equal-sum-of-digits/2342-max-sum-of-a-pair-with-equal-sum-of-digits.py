class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        D = defaultdict(list)

        for i in range(len(nums)):
            s = 0
            n = nums[i]
            while nums[i]:
                s += nums[i] % 10
                nums[i] //= 10
            D[s].append(n)

        result = -1
        for k in D:
            if len(D[k]) >= 2: 
                D[k].sort(reverse= True)
                D[k] = D[k][:2]
                result = max(result,sum(D[k]))

        return(result)