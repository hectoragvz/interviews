# Search in Rotated Sorted Array


def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[left]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
