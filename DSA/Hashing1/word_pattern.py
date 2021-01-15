"""
Algorithm:

split the str into list of strings

if len of pattern unequal with len of str list return False

take each char in pattern and add it as key in dictionary and
corresponding string as value in dict iff both are not present
as key and value respectively

if key is not present from pattern char or their corresponding
str doesnt match as value return False

Time complexity O(1)

Space complexity is O(N) where N is number of unique character
in pattern
"""


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strings = str.split()
        if len(strings) != len(pattern):
            return False

        mapping = {}
        seen = set()

        for c1, c2 in zip(pattern, strings):
            if c1 in mapping and mapping[c1] != c2:
                return False
            elif c1 not in mapping and c2 in seen:
                return False
            else:
                mapping[c1] = c2
                seen.add(c2)

        return True
