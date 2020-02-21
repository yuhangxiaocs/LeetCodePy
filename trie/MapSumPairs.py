'''
    思路是使用字典树，每次插入时更新权重，使用#来表示那个权重值；
    每次sum的时候，首先根据前缀找到对应的位置（过程中有key不存在就返回0）
    然后对下面所有单词求和，使用递归的方法；或者用迭代也可以，注意只有当前当前构成单词
    也就是含有#才加到结果上
'''
from collections import Iterable


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        p = self.root
        for ch in key:
            if ch not in p:
                p[ch] = {}
            p = p[ch]

        p['#'] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        p = self.root
        # 要考虑key不存在的情况
        for ch in prefix:
            if ch in p:
                p = p[ch]
            else:
                return 0
        self.res = 0

        def calSum(p):
            if not p: return
            if '#' in p:
                self.res += p['#']

            for ch in p:
                if isinstance(p[ch], Iterable):
                    calSum(p[ch])

        calSum(p)

        return self.res


if __name__ == '__main__':
    # Your MapSum object will be instantiated and called as such:
    obj = MapSum()
    obj.insert("apple", 3)
    obj.insert("app", 5)
    param_2 = obj.sum('a')
    print(param_2)
