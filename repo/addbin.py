class solution:
    def addbinary ( self, a: str ,b: str)-> str:
        num1 = int(a ,2)
        mum2 = int(b ,2)
        total = num1 + num2
        return bin(total) [2:]