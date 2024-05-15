# 3 Sum
def threeSum(nums):
    res = []
    # Sort the array
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # Same value as previous
            continue
        # Two pointer for two sum 2 for remainder of the list
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # We don´t have to have the same sum
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
