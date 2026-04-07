def containsDuplicate(nums):
    '''
    Given an integer array nums, return true if any value
    appears at least twice in the array,
    and return false if every element is distinct.
    '''
    newSet = set(nums)
    # Having the same length would mean the original array has no repeated values
    return len(nums) != len(newSet)


print(containsDuplicate([1,2,3,4]))
