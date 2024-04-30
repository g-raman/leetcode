class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        buckets = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in buckets:
                buckets[sorted_string].append(string)
            else:
                buckets[sorted_string] = [string]

        return buckets.values()
