# Time Complexity : O(n) where n is the length of input string
# Space Complexity : O(1) as the dictionary can be of max size 52
# (26 lower case and 26 upper case letters)


class Solution:

    # Solution using HashMap

    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        counts = collections.Counter(s)

        longestPalindrome = 0
        odd = False
        for key, value in counts.items():
            if value % 2 == 0:
                longestPalindrome += value
            else:
                longestPalindrome += value - 1
                odd = True

        return longestPalindrome + 1 if odd else longestPalindrome


"""
Algorithm
time complexity O(n)
Space Complexity O(n)
-if char already exist in dictionary increase count by
two and remove that element
-if char not in set add that in set
-at the end if the set is not empty add 1 to the count



class Solution:
    def longestPalindrome(self, s: str) -> int:

        # Using HashSet
        if s is None or len(s) == 0:
            return 0
        set1 = set()
        count = 0
        for i in range(len(s)):
            if s[i] in set1:
                count += 2
                set1.remove(s[i])
            else:
                set1.add(s[i])
        if set1:
            count += 1
        return count

"""
