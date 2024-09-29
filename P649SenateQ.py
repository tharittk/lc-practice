class Solution(object):
    def __init__(self):
        self.senate = []
        self.n = 0
    def predictPartyVictory(self, senate):
    
        """
        :type senate: str
        :rtype: str
        """
        def get_id_to_ban(self, i):
            my_party = self.senate[i]
            j = (i + 1) % self.n
            while self.senate[j] == my_party or self.senate[j] == '-':
                j = (j + 1) % self.n
                if j == i: # no other party left
                    return -1
            return j
        
        self.senate = [s for s in senate]
        self.n = len(senate)
        if self.n == 1:
            return 'Radiant' if senate[0] == 'R' else 'Dire'
        i = 0
        id_ban = get_id_to_ban(self, i)
        while id_ban != -1:
            self.senate[id_ban] = '-'
            i = (i + 1) % self.n
            while self.senate[i] == '-':
                i = (i + 1) % self.n
            id_ban = get_id_to_ban(self, i)

        return 'Radiant' if senate[i] == 'R' else 'Dire'
