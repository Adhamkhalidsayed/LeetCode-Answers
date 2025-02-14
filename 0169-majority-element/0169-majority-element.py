class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict()

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        m,n = 0,0
        for k in d:
            if d[k] > m:
                m = d[k]
                n = k
        return n
