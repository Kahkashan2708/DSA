class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums.append(nums[i])
        ans = nums
        
        return ans            
        