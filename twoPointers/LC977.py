# Squares of a Sorted Array


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    newArray = []

    while left <= right:
        if nums[right] ** 2 > nums[left] ** 2:
            newArray.append(nums[right] ** 2)
            right -= 1

        else:
            newArray.append(nums[left] ** 2)
            left += 1

    return newArray[::-1]


print(sortedSquares(nums=[-7, -3, 2, 3, 11]))
