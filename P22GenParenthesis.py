class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.collect = []

        def aux(self, quota, present, currString):
            if quota == 0:
                tail = ""
                for i in range(present):
                    tail += ")"
                self.collect.append(currString + tail)
            elif present == 0:
                aux(self, quota - 1, 1, currString + "(" )
            else:
                aux(self, quota, present - 1, currString + ")") # match (
                aux(self, quota - 1, present + 1, currString + "(") # generate more

        aux(self, n, 0, "")