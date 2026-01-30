def twoSum(nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return i,j
nums = [3,2,4]
target = 6
print("Ket qua: ", twoSum(nums,target))