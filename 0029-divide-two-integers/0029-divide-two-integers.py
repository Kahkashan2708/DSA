class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max = 2**31-1
        int_min = -2**31

        if dividend == int_min and divisor == -1:
            return int_max
        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp <<1):
                temp <<=1
                multiple <<=1
            dividend -=temp
            quotient += multiple
        return -quotient if negative else quotient            