from collections import Iterable

'''
    这个方法确实好啊 先排序 然后每次添加到set中的时候 如果前缀在 才添加 真巧妙
'''


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        words.sort()

        word_set, longest = set([""]), ""

        for word in words:

            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest


if __name__ == '__main__':
    obj = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    # words = ["w", "wo", "wor", "worl", "world"]
    # words = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"]
    # words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    print(obj.longestWord(words))
    x = "x"
    print(x[:-1] == None)
