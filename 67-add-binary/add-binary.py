class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        sum_decimal = int(a,2)+int(b,2)

        return bin(sum_decimal)[2:]