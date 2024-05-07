def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    maxValue = sum(nums[:k])
    testMax = maxValue

    for i in range(len(nums)):
        if i - k >= 0:
            print(
                f"maxValue is {maxValue}, adding {nums[i]} and subtracting {nums[i-k]}"
            )
            maxValue = maxValue + nums[i] - nums[i - k]
            testMax = max(maxValue, testMax)

    res = float(testMax) / float(k)
    return res


print(findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
