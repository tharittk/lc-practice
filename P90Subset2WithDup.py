class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        h = {}
        for num in nums:
            if not num in h.keys():
                h[num] = 1
            else:
                h[num] += 1
        
        res = []
        
        def aux(uKeys, h, idx, acc):
            res.append(acc.copy())
            for i in range(idx, len(uKeys)):
                for c in range(1, h[uKeys[i]] + 1):
                    aux(uKeys, h, i + 1, acc + ([uKeys[i]] * c))

            return res

        uniq_k = list(h.keys())

        return aux(uniq_k, h, 0, [])
