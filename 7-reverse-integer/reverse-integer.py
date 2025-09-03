class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = int(str(x_abs)[::-1])
        rev = sign * rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev        