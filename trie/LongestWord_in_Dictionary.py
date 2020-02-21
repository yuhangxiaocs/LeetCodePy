class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) < 2: return ''
        words.sort()
        print(words)
        res = []
        for i in range(1, len(words) - 1):
            if words[i].startswith(words[i - 1]):
                if not words[i + 1].startswith(words[i]): res.append(words[i])

        if words[-1].startswith(words[-2]):
            res.append(words[-1])

        maxL = -1
        for i in res:
            maxL = max(maxL, len(i))

        for i in res:
            if len(i) == maxL:
                return i

        return ''


if __name__ == '__main__':
    obj = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    words = ["w", "wo", "wor", "worl", "world"]
    words = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"]
    words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    print(obj.longestWord(words))
