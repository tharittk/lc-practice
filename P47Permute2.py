class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.collect = set()

        def aux(self, curr, stock):
            if not stock:
                self.collect.add(curr)
            else:
                for i in range(len(stock)):
                    curr += (stock[i], )
                    aux(self, curr, stock[:i] + stock[i+1:])
                    curr = curr[:-1]

        aux(self, (), nums)

        out = []

        for permute in self.collect:
            out.append(list(permute))
        return out

        