class Soution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Algorithm

        add each char of s as dict key and corresponding
        index char of t to keys iff those key and value not already present in dict
        if already present check if d[s[i]]=t[i]
        Time complexity o(1)
        space complexity O(2n) that is O(n) where n is unique key value pair
        """
        d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d and t[i] not in d.values():
                d[s[i]] = t[i]
                print(d)
            else:
                if s[i] not in d or d[s[i]] != t[i]:
                    return False
        return True


# More Pythonic Approach:
"""
 Time Complexity : O(n) where n is the length of input string
(as both strings have to be of the same length)
Space Complexity : O(2n) as we require two DS i.e. HashMap and Set
but both datastructures can be of max length 26 as it only
contains all unique letters => O(1)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}
        seen = set()

        for c1, c2 in zip(s, t):
            if c1 in mapping and mapping[c1] != c2:
                return False
            elif c1 not in mapping and c2 in seen:
                return False
            else:
                mapping[c1] = c2
                seen.add(c2)

        return True
