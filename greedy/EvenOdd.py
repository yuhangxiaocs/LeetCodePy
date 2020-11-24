'''
    1217. Minimum Cost to Move Chips to The Same Position
    https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
    vim缩进：crtl+v 按列选择 然后操作即可
'''


def minCostToMoveChips(self, position):
    """
    :type position: List[int]
    :rtype: int
    """
    odd = 0
    even = 0
    
    for pos in position:
        if pos & 1:
            odd += 1
        else:
            even += 1
            
    return min(odd, even)
