class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return

        dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        res = []

        def dfs(digit, index, path, res):

            if index == len(digit):
                res.append(path)
                return

            for ch in dic[int(digit[index])]:
                dfs(digit, index + 1, path + ch, res)

        dfs(digits, 0, "", res)

        return res


if __name__ == '__main__':
    print(Solution().letterCombinations("23434"))
