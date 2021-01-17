"""
Time Complexity : O(n)- as we are iterating through the string,
all other operations are O(1)
Space Complexity : O(n)

Algorithm:

For this solution, I will use a dictionary. It is almost the same as
contigous array question. Here at every point

we are calculating the running sum and check if it is present in
the dictionary or not.

If it is present, just increase its count, otherwise set it to one.
Also, we will check (runnig sum-k) is in the dictionary or not.
If it is already present, that means, sum k has occured again,
so will increment count with value of d[summ-k]
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0
        d = {0: 1}
        count = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            if (summ - k) in d:
                count += d[summ - k]
            if summ in d:
                d[summ] += 1
            else:
                d[summ] = 1
        return count


"""
Same solution in a Pythonic Way

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #optimized
        sum_counts = {0: 1}
        running_sum = 0
        ans = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            ans += sum_counts.get(running_sum-k, 0)
            sum_counts[running_sum] = sum_counts.get(running_sum, 0) + 1

        return ans
"""

#        brute force - TC - O(n^2), SC - O(1)
#         ans = 0
#         for i in range(len(nums)):
#             running_sum = 0
#             for j in range(i, len(nums)):
#                 running_sum += nums[j]
#                 if running_sum == k:
#                     ans += 1

#         return ans
