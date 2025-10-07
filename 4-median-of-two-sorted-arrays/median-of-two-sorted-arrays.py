class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while True:
            i = (left + right) // 2  
            j = half - i             

            nums1_left = nums1[i - 1] if i > 0 else float("-infinity")
            nums1_right = nums1[i] if i < m else float("infinity")
            nums2_left = nums2[j - 1] if j > 0 else float("-infinity")
            nums2_right = nums2[j] if j < n else float("infinity")

            # Check if partitions are correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Odd total length
                if total % 2:
                    return float(min(nums1_right, nums2_right))
                # Even total length
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

        