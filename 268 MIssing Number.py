# https://leetcode.com/problems/missing-number/submissions/1790992758/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        x = 0
        for num in nums:
            x ^= num
        for i in range(len(nums)+1):
            x ^= i

        return x