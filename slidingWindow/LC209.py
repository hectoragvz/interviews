# Minumum Size Subarray Sum


def minSubArrayLen(self, target, nums):

    if sum(nums) < target:
        return 0

    minLen = len(nums)
    left = 0
    sumLen = 0

    for right in range(len(nums)):
        sumLen = sumLen + nums[right]
        while sumLen >= target:
            minLen = min(minLen, right - left + 1)
            sumLen = sumLen - nums[left]
            left += 1

    return minLen


print(minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
