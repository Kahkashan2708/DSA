class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        max_num = max(nums)+1
        for  i in range(0, max_num+1):
            if i not in nums:
                return i
            else:
                i+=1    
        