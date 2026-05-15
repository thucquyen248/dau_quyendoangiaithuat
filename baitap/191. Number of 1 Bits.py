class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            # remove the lowest set bit
            n &= (n - 1)
            count += 1
        return count
