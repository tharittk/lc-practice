class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        def process_white_space(s):
            i = 0
            while i < len(s) and s[i] == " ":
                i += 1
            return s[i:]
        
        def check_overflow(a, x, is_negative):
            if not is_negative:
                if a > 2147483647 - x:
                    return True
            else:
                if a > 2147483648 - x:
                    return True
            
            return False

        if not s:
            return 0
        s = process_white_space(s)    
        if not s:
            return 0
        i = 0
        is_negative = False
        
        if s[i] == '-':
            is_negative = True
            i += 1
        elif s[i] == '+':
            i += 1
        elif s[i].isnumeric():
            pass
        else:
            return 0
        s = s[i:]
        if not s:
            return 0
        i = 0
        if not s[i].isnumeric():
            return 0
        else:
            out = 0
            while i < len(s) and s[i].isnumeric():
                digit = ord(s[i]) - ord('0')
                #print(digit)
                is_overflow = check_overflow(out, digit, is_negative)
                if is_overflow:
                    return -2147483648 if is_negative else 2147483647
                out *= 10
                is_overflow = check_overflow(out, digit, is_negative)
                if is_overflow:
                    return -2147483648 if is_negative else 2147483647
                out += digit
                i += 1
            return -out if is_negative else out



        
