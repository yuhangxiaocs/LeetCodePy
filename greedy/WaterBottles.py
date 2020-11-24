'''
    1518. Water Bottles
    https://leetcode.com/problems/water-bottles/
    小学生难度
'''

def numWaterBottles(self, numBottles, numExchange):
    res = numBottles
    while numBottles >= numExchange:
        full = numBottles / numExchange
        numBottles = numBottles % numExchange + full
        res += full
    return res
