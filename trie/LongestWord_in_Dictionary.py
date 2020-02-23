# class Solution(object):
# def longestWord(self, words):
#     """
#     :type words: List[str]
#     :rtype: str
#     """
#     if len(words) < 2: return ''
#     words.sort()
#     print(words)
#     res = []
#     for i in range(1, len(words) - 1):
#         if words[i].startswith(words[i - 1]):
#             if not words[i + 1].startswith(words[i]): res.append(words[i])
#
#     if words[-1].startswith(words[-2]):
#         res.append(words[-1])
#
#     maxL = -1
#     for i in res:
#         maxL = max(maxL, len(i))
#
#     for i in res:
#         if len(i) == maxL:
#             return i
#
#     return ''
from collections import Iterable


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # print(sorted(words))
        self.root = {}

        def insert(word):
            p = self.root
            for ch in word:
                if ch not in p: p[ch] = {}
                p = p[ch]
            p['#'] = True

        for word in words:
            insert(word)

        self.res = []

        def dfs(p, path):
            if '#' in p:
                self.res.append(path)
            for ch in p:
                if isinstance(p[ch], Iterable):
                    if '#' in p[ch]:
                        dfs(p[ch], path + ch)

        dfs(self.root, "")
        maxL = -1
        self.res.sort()
        for i in self.res:
            maxL = max(maxL, len(i))
        for i in self.res:
            if len(i) == maxL:
                return i


if __name__ == '__main__':
    obj = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    # words = ["w", "wo", "wor", "worl", "world"]
    # words = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"]
    # words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    print(obj.longestWord(words))
