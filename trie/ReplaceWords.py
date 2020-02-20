'''
    Runtime: 56 ms, faster than 98.60% of Python3 online submissions for Replace Words.
    Memory Usage: 27.3 MB, less than 60.00% of Python3 online submissions for Replace Words.

    要注意的是 那个#到底是在哪里的
'''


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.root = {}

        def insert(word):
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

        def replace(word):

            r = ""
            p = self.root
            for ch in word:
                if ch in p:
                    r += ch
                    p = p[ch]
                    if '#' in p: return r
                else:
                    break
            # 如果没有则返回本身
            return word

        for ch in dict:
            insert(ch)

        res = ""

        s = sentence.split(sep=' ')

        for ch in s:
            res += replace(ch) + ' '

        return res.rstrip()
