import math

class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # đổi sang chỉ số 0-based
        res = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            res.append(nums[index])
            nums.pop(index)
            k %= fact
        
        return "".join(res)