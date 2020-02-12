class Solution:
    # @param n, an integer
    # @return an integer
    '''
        这里是一个常见问题，是否需要break，在最后一次完成后，是不需要再移位的，所以要break
    '''
    def reverseBits(self, n):

        res = 0
        for i in range(32):
            bit = n & 1

            res = res | bit
            if i == 31: break

            res = res << 1
            n = n >> 1

        return res
