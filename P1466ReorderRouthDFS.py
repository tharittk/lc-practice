class Solution(object):
    def minReorder(self, n, connections):
        self.visited = [False for i in range(n)]
        self.pointsTo = [[] for i in range(n)]
        self.pointedBy = [[] for i in range(n) ]
        self.q =[]
        self.count = 0
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        def dfs_count_and_push(node):
            self.visited[node] = True
            for incoming in self.pointedBy[node]:
                if not self.visited[incoming]:
                    self.q.append(incoming)
            for outgoing in self.pointsTo[node]:
                if not self.visited[outgoing]:
                    self.count += 1
                    dfs_count_and_push(outgoing)
        for connection in connections:
            head = connection[0]
            tail = connection[1]
            self.pointsTo[head].append(tail)
            self.pointedBy[tail].append(head)

        self.q = []
        self.q.append(0)
        while (self.q):
            dfs_count_and_push(self.q.pop(0))
        return self.count

