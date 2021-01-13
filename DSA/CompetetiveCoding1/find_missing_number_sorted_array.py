class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0

        while high - low >= 2:

            mid = low + (high - low) // 2

            mid_index_diff = nums[mid] - mid
            low_index_diff = nums[low] - low

            if mid_index_diff != low_index_diff:
                high = mid

            else:
                low = mid

        return round((nums[low] + nums[high]) / 2)


"""
Another Solution
#Time Complexity : O(logn) where n is length of input array
#Space Complexity : O(1) no auxilary space is used

class Solution:
    def missingNumber(self, nums):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            #numbers on the left are all in the correct position so we look only on the right side
            if nums[mid] == mid:
                left = mid + 1
            #numbers on the right are all in the correct position so we look only on the left side
            else:
                right = mid - 1

        #smallest number which is in the incorrect position thus it's index is the missing number
        return left

"""
