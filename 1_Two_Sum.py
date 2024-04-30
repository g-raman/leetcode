class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]

            seen[nums[i]] = i

        return []
