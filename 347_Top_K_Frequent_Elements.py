class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        seen_count = {}

        for num in nums:
            if num in seen_count:
                seen_count[num] += 1
            else:
                seen_count[num] = 1

        sorted_seen_count = sorted(seen_count.items(), key=lambda a: a[1], reverse=True)

        results = []
        for i in range(0, k):
            results.append(sorted_seen_count[i][0])
        return results
