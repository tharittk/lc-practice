class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        hmap = {}
        for num in candidates:
            if not num in hmap.keys():
                hmap[num] = 1
            else:
                hmap[num] += 1

        res = []

        def aux(uniq_candidates, hmap, idx, acc, currSum):
            if currSum > target: # stop early
                return
            if currSum == target:
                res.append(acc.copy())
                return 
            for i in range(idx, len(uniq_candidates)):
                candid = uniq_candidates[i]
                for c in range(1, hmap[candid] + 1):
                    aux(uniq_candidates, hmap, i + 1, acc + [candid] * c, currSum + candid * c)
                # next iter = candid[i] discarded i.e. not taken
        aux(list(hmap.keys()), hmap, 0, [], 0)

        return res




