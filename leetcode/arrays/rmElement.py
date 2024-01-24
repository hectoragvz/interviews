def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1

    return l


print(removeElement([3,2,2,3], 3))