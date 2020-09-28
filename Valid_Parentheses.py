# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        n = len(s)
        if n < 2: return False
        for i in range(n):
            if s[i] in ["(", "{", "["]:
                res.append(s[i])
            elif s[i] == ")" and res and res[-1] == "(":
                res.pop()
            elif s[i] == "}" and res and res[-1] == "{":
                res.pop()
            elif s[i] == "]" and res and res[-1] == "[":
                res.pop()
            else: 
                return False
        return len(res) == 0