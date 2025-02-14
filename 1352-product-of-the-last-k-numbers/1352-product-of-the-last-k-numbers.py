class ProductOfNumbers:

    def __init__(self):
        self.lst = []
        self.product = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.lst.append(self.product)
        else:
            self.product = 1
            self.lst = []
        
    

    def getProduct(self, k: int) -> int:
        if k > len(self.lst):
            return 0
        elif k == len(self.lst):
            return self.product
        else:
            return int(self.lst[-1]/self.lst[-1-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)