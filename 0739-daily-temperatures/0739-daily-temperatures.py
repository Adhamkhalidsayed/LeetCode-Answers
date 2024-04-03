class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackIndex, stackTemp = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append((index,temp))
        return result