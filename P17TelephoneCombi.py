class Solution(object):
    def __init__(self):
        self.combinations = []
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def get_combination (curr, digits, i):
            if i == len(digits):
                self.combinations.append(curr)
            else:
                for j in range(run_range(digits[i])):
                    c =  getCharAt(digits[i], j)
                    curr += c
                    get_combination(curr, digits, i+1)
                    curr = curr[:-1]
    

    
        def getCharAt(num, i):
                if num == '2':
                    return "abc"[i]
                elif num ==  '3':
                    return "def"[i]
                elif num ==  '4':
                    return "ghi"[i]
                elif num == '5':
                    return "jkl"[i]
                elif num == '6':
                    return "mno"[i]
                elif num == '7':
                    return "pqrs"[i]
                elif num == '8':
                    return "tuv"[i]
                elif num == '9':
                    return "wxyz"[i]
        def run_range(num):
            if num == '7' or num == '9':
                return 4
            else:
                return 3
        if digits == "":
            return ""
        get_combination('', digits, 0)

        return self.combinations
