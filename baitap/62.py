import math

class Solution:
    def uniquePaths(self, m, n):
        return self.comb(m + n - 2, m - 1)

    def comb(self, n, r):
        # Efficient computation of nCr without math.comb
        r = min(r, n - r)  # symmetry
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator *= (n - i)
            denominator *= (i + 1)
        return numerator // denominator