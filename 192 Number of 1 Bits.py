# https://leetcode.com/problems/number-of-1-bits/submissions/1791023871/?envType=problem-list-v2&envId=bit-manipulation

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n & 1:
                count+=1
            n >>= 1
        return count


        


S = Solution()
print(S.hammingWeight(11))