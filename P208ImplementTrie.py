class Trie:

    def __init__(self):
        self.trie = [{}, None]        

    def insert(self, word: str) -> None:
        node = self.trie
        for i in range(len(word)-1):
            c = word[i]
            if c in node[0].keys():
                node = node[0][c]
            else:
                node[0][c] = [{}, None]
                node = node[0][c]
        i = len(word) - 1
        c = word[i]
        if c in node[0].keys():
            node[0][c] = [node[0][c][0], 1] # copy old chain
        else:
            node[0][c] = [{}, 1]
        

    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c in node[0].keys():
                node = node[0][c]
            else:
                return False
        return node[1] == 1

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c in node[0].keys():
                node = node[0][c]
            else:
                return False     
        return True       
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
