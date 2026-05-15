class Solution:
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        # keep shifting until left == right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
