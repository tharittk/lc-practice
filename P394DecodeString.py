class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expandStringFrom(i, s):

            num = ''
            while s[i].isnumeric():
                num += s[i]
                i += 1
            k = int(num)
            st, ibracket = accumulateString(i, s)
            out = k * st

            return out, ibracket
        
        def accumulateString(i, s):
            assert s[i] == '['
            i += 1
            out = ''
            while s[i] != ']':
                if s[i].isnumeric():
                    st, ibracket = expandStringFrom(i, s)
                    out += st
                    i = ibracket + 1
                else:
                    out += s[i]
                    i +=1
            return out, i

        i = 0
        out = ''
        while i < len(s):
            if s[i].isnumeric():
                st, i = expandStringFrom(i, s)
                out += st
                i += 1
            else:
                out += s[i]
                i +=1
        
        return out

