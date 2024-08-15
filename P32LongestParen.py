class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        stack = []
        n = []
        out = []
        count = 1
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                n.append(count)
                count += 1
            elif s[i] == ")":
                if stack == []:
                    count += 1
                else:
                    stack.pop()
                    out.append(n.pop())
        out.sort()

        if out == []:
            return 0
        if len(out) == 1:
            return 2
        i = 0
        maxlen = 1
        ln = 1
        for i in range(len(out) - 1):
            if out[i] + 1 == out[i+1]:
                ln += 1
                if ln > maxlen:
                    maxlen = ln
            else:
                ln = 1

        return 2*maxlen
        

        