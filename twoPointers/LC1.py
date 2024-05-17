# Two SUm


def twoSum(nums, target):
    elements = {}

    for i in range(len(nums)):
        lookup = target - nums[i]
        if lookup in elements:
            return [i, elements[lookup]]
        else:
            elements[nums[i]] = i


print(twoSum(nums=[3, 3], target=6))
