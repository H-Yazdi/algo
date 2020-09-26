class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not s: return 0

        res = [0 for i in range(n + 1)] 
        res[0] = 1 
         
        if s[0] == "0":
            res[1] = 0
        else :
            res[1] = 1

        for i in range(2, n + 1): 
            if 0 < int(s[i-1:i]) <= 9:    
                res[i] += res[i - 1]
            if 10 <= int(s[i-2:i]) <= 26: 
                res[i] += res[i - 2]
        return res[n]
