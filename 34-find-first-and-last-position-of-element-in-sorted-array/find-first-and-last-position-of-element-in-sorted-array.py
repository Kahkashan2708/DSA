class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    idx = mid
            return idx

        return [findLeft(nums, target), findRight(nums, target)]
