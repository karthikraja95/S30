# Time Complexity : O(nk) where n is number of strings in given array
# and k is length of longest string in array
# Space Complexity : O(nk) where n is number of unique strings in given
# y and k is number of strings for each unique string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimized:
        primes = []
        possiblePrime = 2
        while len(primes) != 26:
            isPrime = True
            for num in range(2, possiblePrime):
                if possiblePrime % num == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(possiblePrime)
            possiblePrime += 1

        def primeProducts(s):
            result = 1
            for char in s:
                result *= primes[ord(char) - ord("a")]

            return result

        anagrams = collections.defaultdict(list)
        for word in strs:
            code = primeProducts(word)
            anagrams[code].append(word)

        return anagrams.values()
        # anagrams = collections.defaultdict(list)
        #
        # for word in strs:
        #     sword = "".join(sorted(word))
        #     anagrams[sword].append(word)
        #
        # return anagrams.values()
