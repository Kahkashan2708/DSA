class Solution(object):
    def isValid(self, s):
        mapping = {')':'(', '}': '{', ']': '[' }
        stack = []

        for i in s:
            if i in mapping:
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                else:    
                    return False
            else:
                stack.append(i)
                
        return not stack                
        