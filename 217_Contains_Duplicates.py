class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
