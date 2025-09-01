class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        
        # Convert number to string and check if it reads same backwards
        return str(x) == str(x)[::-1]
        