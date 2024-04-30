class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        letter_count = {}
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        for letter in t:
            if letter not in letter_count:
                return False
            letter_count[letter] -= 1

        for letter in letter_count:
            if letter_count[letter] != 0:
                return False
        return True
