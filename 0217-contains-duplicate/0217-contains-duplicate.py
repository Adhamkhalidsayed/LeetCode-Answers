class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Q = set()
        for i in nums:
            if i in Q:
                return True
            Q.add(i)
        return False
            
                    