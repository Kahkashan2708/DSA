class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, res = 0, ""
        
        while i < len(word1) and i < len(word2):
            res += word1[i] + word2[i]
            i += 1
        return res + word1[i:] + word2[i:]
    



