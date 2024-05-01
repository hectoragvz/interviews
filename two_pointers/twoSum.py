def twoSum(nums, target):
    sol = []
    seenNums = {}

    for index in range(len(nums)):
        if target - nums[index] in seenNums:
            return [index, seenNums[target - nums[index]]]
        else:
            seenNums[nums[index]] = index

    return sol


print(twoSum(nums=[3, 2, 4], target=6))
