# Maximum Average Subarray 1


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    maxValue = sum(nums[:k])
    testMax = maxValue

    left = 0
    for right in range(k, len(nums)):
        maxValue = maxValue + nums[right] - nums[left]
        testMax = max(maxValue, testMax)
        left += 1

    res = float(testMax) / float(k)
    return res


print(findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
