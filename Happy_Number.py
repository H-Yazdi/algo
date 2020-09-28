# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n):
            if n <10 :
                return n **2
            else: 
                r = n % 10
                m = n / 10
            return helper(r) + helper(m)
        seen = set()
        while True: 
            if helper(n) == 1: return True
            elif helper(n) in seen : return False
            else: seen.add(helper(n))
            n = helper(n)