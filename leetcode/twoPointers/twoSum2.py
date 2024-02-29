def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    sol = []
    left = 0
    right = len(numbers) - 1

    while left < right:
        if (numbers[left] + numbers[right]) == target:
            sol.append(left + 1)
            sol.append(right + 1)
            return sol
        elif (numbers[left] + numbers[right]) < target:
            left += 1
        elif (numbers[left] + numbers[right]) > target:
            right -= 1


print(twoSum([-1,0], -1))