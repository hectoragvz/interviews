def findMin(nums):
    left, right = 0, len(nums) - 1
    res = float("inf")

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] > nums[right]:
            # Mid is in the upper part
            res = min(nums[right], res)
            left = mid + 1
        else:
            res = min(res, nums[mid])
            right = mid - 1
    return res


print(findMin([3, 4, 5, 1, 2]))
