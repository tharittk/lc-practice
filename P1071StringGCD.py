class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        tmp = str1
        if len(str2) > len(str1):
            str1 = str2
            str2 = tmp

        max_len = len(str2)

        for i in range(max_len, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                sub_str2 = str2[:i]
                mul_get2 = len(str2) // i
                mul_get1 = len(str1) // i
                if sub_str2 * mul_get2 == str2 and sub_str2 * mul_get1 == str1:
                    return sub_str2
            else:
                continue
        return ''
            
