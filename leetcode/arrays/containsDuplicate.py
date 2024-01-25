def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    uniques = set()
    for i in range(len(nums)):
        if nums[i] not in uniques:
            uniques.add(nums[i])
        else:
            return True
    return False
