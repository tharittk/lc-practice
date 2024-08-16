class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        Tries = {}
        
        # build
        for num in arr1:
            snum = str(num)
            i = 0
            dd = Tries
            while i < len(snum):
                if snum[i] not in dd.keys():
                    dd[snum[i]] = {}
                dd = dd[snum[i]]
                i += 1
        
        # search
        maxlen = 0
        for num in arr2:
            snum = str(num)
            i = 0
            dd = Tries
            while i < len(snum):
                if snum[i] in dd.keys():
                    dd = dd[snum[i]]
                    i +=1
                else:
                    break

            if i > maxlen:
                maxlen = i
    
        return maxlen
        
