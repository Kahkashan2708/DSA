class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                num = s[l]
                s[l] = s[r]
                s[r] = num

            l, r = l+1, r-1    
        