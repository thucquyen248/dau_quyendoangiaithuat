from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert all numbers to strings
        nums = list(map(str, nums))
        
        # Custom comparator: order by concatenation result
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join into one string
        result = ''.join(nums)
        
        # Edge case: leading zeros (e.g. [0,0])
        return '0' if result[0] == '0' else result
