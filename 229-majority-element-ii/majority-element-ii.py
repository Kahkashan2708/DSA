class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, count in count.items():
            if count > len(nums)// 3:
                res.append(num)

        return res        
