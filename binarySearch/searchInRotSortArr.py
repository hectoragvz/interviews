def searchInRotSortArr(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[right]:
            # Upper portion
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Down portion
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(searchInRotSortArr([4, 5, 6, 7, 0, 1, 2], 0))
