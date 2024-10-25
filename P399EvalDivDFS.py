class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        G = {}
        for i in range(len(equations)):
            v1, v2 = equations[i][0], equations[i][1]

            if not v1 in G.keys():
                G[v1] = [(v2, values[i])]
            else:
                G[v1].append((v2, values[i]))
            
            if not v2 in G.keys():
                G[v2] = [(v1, 1/values[i])]
            else:
                G[v2].append((v1, 1/values[i]))

        def init_visit(G):
            visited = {}
            for v in list(G.keys()):
                visited[v] = False
            return visited

        def dfs(G, visited, start, target, acc):
            visited[start] = True
            if start == target:
                return acc
            for v, e in G[start]:
                if not visited[v]:
                    res = dfs(G, visited, v, target, acc * e)
                    if res:
                        return res
        out = []
        for q in queries:
            start, end = q[0], q[1]
            if not start in G.keys() or not end in G.keys():
                out.append(-1.0)
            else:
                visited = init_visit(G)
                res = dfs(G, visited, q[0], q[1], 1)
                if res:
                    out.append(res)
                else:
                    out.append(-1.0)
        return out


