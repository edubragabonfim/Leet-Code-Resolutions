class Solution(object):
    def numberOfSteps_1Solution(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num%2:
                num -= 1
            else:
                num//= 2
            steps+=1
        return steps
    
    def numberOfSteps_2Solution(self, num):  # Using Bitwise Operators
        steps = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num>>=1
            steps+=1
        return steps
        
