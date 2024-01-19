# Iterative method

def binary_sarch(array, target):
    # defining indexes to look for
    left = 0  # min index
    right = len(array) - 1  # last index since start at 0

    while left <= right:
        # midpoint index
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        if array[mid] < target:
            left = mid + 1
        else:
            # Return index of target num
            return mid
    # target not foud in the array
    return -1


print(binary_sarch([-1, 0, 3, 5, 9, 12], 9))
