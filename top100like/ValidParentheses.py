class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        characters = list(s)
        print(characters)
        # 哨兵 接下来就不用判断stack是否为空了
        stack = ['#']
        for ch in characters:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                print("dfa")
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            # 最后这个else是不能少的 比如输入]的时候 如果没有这一行 就不会进入stack中
            else:
                stack.append(ch)

        return len(stack) == 1


if __name__ == '__main__':
    print(Solution().isValid("]"))
