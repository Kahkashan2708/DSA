class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l_1, l_2 = len(word1), len(word2)
        res = ""
        if l_1 == l_2:
            for i in range(l_1):
                res += word1[i]
                res += word2[i] 

        elif l_1 < l_2:
            for i in range(l_1):
                res += word1[i]
                res += word2[i]
            res+= word2[i+1 :]   
        else:
            for i in range(l_2):
                res += word1[i]
                res += word2[i]
            res+= word1[i+1 :]

        return res    



