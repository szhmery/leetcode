class Trie:
    # https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "#" in cur


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":

    obj = Trie()
    obj.insert("apple")
    param_2 = obj.search("apple")
    param_3 = obj.startsWith("app")
    print(param_2)
    print(param_3)