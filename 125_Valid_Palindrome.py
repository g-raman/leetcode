class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        start = 0
        end = len(s) - start - 1
        lowercase_str = s.lower()

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif lowercase_str[start] != lowercase_str[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
