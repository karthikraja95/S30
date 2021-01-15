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
