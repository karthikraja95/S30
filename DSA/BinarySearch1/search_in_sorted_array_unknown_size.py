# Time Complexity : O(logn) where n is the index of the value we are searching for
# Space Complexity : O(1)


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        # find boundaries
        while reader.get(right) < target:
            left = right
            right *= 2

        while left <= right:
            pivot = left + ((right - left) // 2)
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1
