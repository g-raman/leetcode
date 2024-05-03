class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = len(numbers) - 1
        while start < end:
            curr_sum = numbers[start] + numbers[end]

            if curr_sum < target:
                start += 1
            elif curr_sum > target:
                end -= 1
            else:
                return [start + 1, end + 1]
