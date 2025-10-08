class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words =[]
        
        for word in s.split():
            words.append(word)

        length = len(words[-1])

        return length    