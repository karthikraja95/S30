# Time Complexity : O(logn)
# Space Complexity : O(1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if not nums:
            return None

        left, right = 0, len(nums) - 1

        if len(nums) < 2:
            return left if nums[left] >= nums[right] else right

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left
