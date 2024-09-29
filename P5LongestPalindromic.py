class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.cache = {}
        def aux(self, head, tail):
            # base case
            if head == tail:
                return self.s[head]
            if head == tail + 1:
                return ""
            if (head, tail) in self.cache:
                return self.cache[(head, tail)]

            cut_head = aux(self, head+1, tail)
            cut_tail = aux(self, head, tail - 1)
            if self.s[head] == self.s[tail]:
                inner = aux(self, head + 1, tail - 1)
                if len(inner) == (tail - head - 1): # this case always wins
                    self.cache[(head, tail)] = (self.s[head] + inner + self.s[tail])
                    return self.cache[(head, tail)]
            # if head, tail not same string, the inner will implcitly be contained in both cut_head and cut_tail
            if len(cut_head) > len(cut_tail):
                self.cache[(head, tail)] = cut_head
            else:
                self.cache[(head, tail)] = cut_tail
            return self.cache[(head, tail)]

        return aux(self, 0, len(s) - 1)

