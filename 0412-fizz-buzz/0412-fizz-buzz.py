class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 0
        lst = []
        while i+1 <= n:
            if ((i+1) % 3 == 0) and ((i+1) % 5 == 0):
                lst.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                lst.append("Fizz")
            elif (i+1) % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(i+1))
            
            i+=1
        return lst
            