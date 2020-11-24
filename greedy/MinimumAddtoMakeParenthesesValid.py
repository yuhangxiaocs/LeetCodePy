class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        stack = []
        r = 0
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if stack:
                    stack.pop()
                else:
                    r += 1
        # print(r)
        # print(stack)

        return len(stack) + r
