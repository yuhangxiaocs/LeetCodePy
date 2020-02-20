'''
    Runtime: 116 ms, faster than 98.66% of Python online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 28 MB, less than 76.47% of Python online submissions for Implement Trie (Prefix Tree).
'''


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root

        for ch in word:
            if ch not in p:
                p[ch] = {}

            p = p[ch]

        # 用这个特殊的标记代表是单词结尾
        p['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root

        for ch in word:
            if ch in p:
                p = p[ch]
            else:
                return False
        return '#' in p

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        p = self.root
        for ch in prefix:
            if ch in p:
                p = p[ch]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
