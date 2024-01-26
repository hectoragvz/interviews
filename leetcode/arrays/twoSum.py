def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    values = {}

    for index, number in enumerate(nums):
        goal = target - number

        if goal in values.keys():
            return [values[goal], index]
        else:
            values[number] = index


# I was scratching for longer than I planned around the fact enumerate was never needed, indeed is easier but your first thought may also be to simply play with nums[i] and i:


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    values = {}

    for i in range(len(nums)):
        goal = target - nums[i]

        if goal in values.keys():
            return [values[goal], i]
        else:
            values[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))
