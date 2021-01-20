"""
Time Complexity : O(m) whene m is numbr of houses
Space Complexity : O(1)

Your code here along with comments explaining your approach:
This is a DP solution in case we can not manipulate the initial array.
At every row, we have memoised what can be the minimum value for red ,
blue and green from the previous value and hence can be used
to find minimum cost after all the rows have been iterated
"""


class Solution:
    def minCost(self, costs):
        # write your code here
        if not costs or costs is None:
            return 0
        m = len(costs)
        # n = len(costs[0])
        cr, cb, cg = 0, 0, 0
        for i in range(0, m):
            cr, cb, cg = (
                costs[i][0] + min(cb, cg),
                costs[i][1] + min(cr, cg),
                costs[i][2] + min(cb, cr),
            )
        return min(cr, cb, cg)
