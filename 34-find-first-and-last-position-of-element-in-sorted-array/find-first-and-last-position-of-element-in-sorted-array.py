class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        left_ind, right_ind = -1, -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left_ind = mid
                right = mid - 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right_ind = mid
                left = mid + 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [left_ind, right_ind]