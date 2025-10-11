class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []

        len1 = len(nums1)
        len2 = len(nums2)

        if len1 >= len2:
            for i in nums2:
                if i not in res and i in nums1:
                    res.append(i)        

        else:
            for i in nums1:
                if i not in res and i in nums2:
                    res.append(i)  

        return res            
