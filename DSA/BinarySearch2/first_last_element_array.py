class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if nums is None or len(nums) == 0:
            return [-1, -1]

        left = self.binary_search_left(nums, target)
        right = self.binary_search_right(nums, target)

        return [left, right]

    def binary_search_left(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            # In Jave we will have integer overflow
            # but doesn't have. Its safer to use
            # low + (high-low)//2 instead of (low+high)//2
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if mid == low or nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def binary_search_right(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            # In Jave we will have integer overflow
            # but doesn't have. Its safer to use
            # low + (high-low)//2 instead of (low+high)//2
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if mid == high or nums[mid] < nums[mid + 1]:
                    return mid
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
