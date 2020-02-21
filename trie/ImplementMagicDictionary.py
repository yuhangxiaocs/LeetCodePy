'''
    用字典把长度相同的字符串都存储起来，search的时候就是把长度匹配的都拿出来看看
'''


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            if len(word) in self.dic:
                self.dic[len(word)].append(word)
            else:
                self.dic[len(word)] = [word]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """

        if len(word) not in self.dic: return False

        for candidate in self.dic[len(word)]:
            diff = 0

            for a, b in zip(candidate, word):
                if a != b: diff += 1

            if diff == 1: return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
