class Solution(object):
    def mySqrt(self, x):
        
        l,r = 1, x//2
        res = 1

        if x<2:
            return x

        while l <= r:
            m = (l+r)//2

            if m*m == x:
                return m
            elif m*m < x:
                res = m 
                l = m + 1
            else:
                r = m-1

        return res        

        