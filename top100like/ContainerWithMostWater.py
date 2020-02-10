class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # for pos i,j
        # area = (j - i) * min(height[i], height[j])

        # maxArea = -1
        # for i in range(len(height) - 1):
        #     for j in range(i, len(height)):
        #         maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
        #
        # return maxArea
        l, r = 0, len(height) - 1
        maxArea = -1
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # find max
        maxHeight = -1
        maxPos = -1

        for i in range(len(height)):
            if height[i] >= maxHeight:
                maxHeight = height[i]
                maxPos = i
        print("pos", maxPos, "max", maxHeight)
        maxL = -1
        maxLPos = maxPos
        for i in range(maxPos, -1, -1):
            if height[i] * (maxPos - i) >= maxL:
                maxL = height[i] * (maxPos - i)
                maxLPos = i

        print("max", maxL, "pos", maxLPos)

        maxR = -1
        maxRPos = maxPos
        for i in range(maxPos, len(height)):
            if height[i] * (i - maxPos) >= maxR:
                maxR = height[i] * (i - maxPos)
                maxRPos = i

        print("max", maxR, "pos", maxRPos)

        a = min(height[maxLPos], height[maxRPos]) * (maxRPos - maxLPos)

        return max(a, max(maxL, maxR))


if __name__ == '__main__':
    a = [8, 10, 14, 0, 13, 10, 9, 9, 11, 11]
    print(len(a))
    print(a)
    print(Solution().maxArea(a))
