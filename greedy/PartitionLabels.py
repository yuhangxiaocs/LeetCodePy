class Solution(object):
    def partitionLabels(self, S):
        dic = {}
        for i, ch in enumerate(S):
            if ch in dic:
                dic[ch][0] = min(dic[ch][0], i)
                dic[ch][1] = max(dic[ch][1], i)
            else:
                dic[ch] = [i, i]
        # print(sorted(dic.values(), key=lambda x: x[0]))

        intervals = sorted(dic.values(), key=lambda x: x[0])
        # print(sorted(dic.values(), key=lambda x: x[1]))

        res = []
        l, r = intervals[0]
        intervals.pop(0)
        intervals.append([float('inf'), float('inf')])
        for a, b in intervals:
            if a > r:
                res.append(r - l + 1)
                l, r = a, b
            else:
                l = min(l, a)
                r = max(r, b)
        return res