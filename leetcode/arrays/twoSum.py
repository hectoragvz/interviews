def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    values = {}

    for index, number in enumerate(nums):
        goal = target - number

        if goal in values.keys():
            return [values[goal], index]
        else:
          values[number] = index    
            
            
print(twoSum([2,7,11,15], 9))