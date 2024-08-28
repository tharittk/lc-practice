class SmallestInfiniteSet(object):

    def __init__(self):
        self.root = 1
        self.minheap = []
        self.set = set()
        

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.minheap:
            top = self.minheap[0]
            if top < self.root:
                self.set.remove(top)
                return heappop(self.minheap)
            else:
                tmp = self.root
                self.root += 1
                return tmp
        else:
            tmp = self.root
            self.root += 1
            return tmp
            

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.root > num: # num used to be removed
            if num not in self.set:
                heappush(self.minheap, num)
                self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)