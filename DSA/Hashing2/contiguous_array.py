"""
Algorithm
Time complexity O(n)
Space Complexity O(n)

if encountered 1 in array add +1 else (0) -1

if the runningSum is already in sum_indices ,
this means that we encountered a subarray with equal 0 and 1
so we need to update maxlength
(current index-sum_indices[runningSum]index)

else add runningSum as key and its index as value

return maxlength
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums is null or len(nums) == 0:
            return 0
        d = {0: -1}  # {count:index}
        maxlen = 0
        rsum = 0
        for i in range(len(nums)):
            rsum += 1 if nums[i] == 1 else -1
            if rsum in d:
                maxlen = max(maxlen, i - d[rsum])
            else:
                d[rsum] = i
        return maxlen


# brute force - TC- O(n^2) SC - O(1)
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         max_len = 0
#
#         for i in range(len(nums)):
#             zeroes, ones = 0, 0
#             for j in range(i, len(nums)):
#                 if nums[j] == 0:
#                     zeroes += 1
#                 else:
#                     ones += 1
#
#                 if zeroes == ones:
#                     max_len = max(max_len, j-i+1)
#
#         return max_len
