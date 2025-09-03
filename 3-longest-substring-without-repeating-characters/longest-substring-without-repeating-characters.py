class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
    
        for i in range(len(s)):
            seen = ""
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen += s[j]
                longest = max(longest, len(seen))
    
        return longest
        