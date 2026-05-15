class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  # handle k larger than n

        # helper to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # reverse the whole array
        reverse(0, n - 1)
        # reverse the first k elements
        reverse(0, k - 1)
        # reverse the remaining elements
        reverse(k, n - 1)
