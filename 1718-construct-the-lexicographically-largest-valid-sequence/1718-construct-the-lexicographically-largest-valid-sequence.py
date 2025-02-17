class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0] * (2*n-1)
        used = set()
        
        def backtrack(i):
            if i == len(arr):
                return True
            
            for num in reversed(range(1, n+1)):
                if num in used:
                    continue
                if num > 1 and ((i + num >= len(arr)) or arr[i + num]):
                    continue
                
                used.add(num)
                arr[i] = num
                if num > 1:
                    arr[i+num] = num
                
                j = i + 1
                while j < len(arr) and arr[j]:
                    j += 1

                if backtrack(j):
                    return True
                
                used.remove(num)
                arr[i] = 0
                if num > 1:
                    arr[i+num] = 0
                
            return False
                
        backtrack(0)
        return arr