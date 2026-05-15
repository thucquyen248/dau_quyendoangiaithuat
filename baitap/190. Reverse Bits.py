class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            # shift result left to make room
            result <<= 1
            # add the least significant bit of n
            result |= (n & 1)
            # shift n right to process next bit
            n >>= 1
        return result
