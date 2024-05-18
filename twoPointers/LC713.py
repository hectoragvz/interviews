# Subarray Product Lees than K


def numSubarrayProductLessThanK(nums, k):

    res = 0
    left = 0
    product = 1

    for right in range(len(nums)):
        product *= nums[right]
        while left <= right and product >= k:
            product = product // nums[left]
            left += 1
        res += right - left + 1

    return res


print(numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
