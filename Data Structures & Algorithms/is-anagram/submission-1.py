class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenOne = {}
        seenTwo = {}

        for char in s:
            seenOne[char] = seenOne.get(char, 0) + 1

        for char in t:
            seenTwo[char] = seenTwo.get(char, 0) + 1

        if seenOne == seenTwo:
            return True
        else:
            return False