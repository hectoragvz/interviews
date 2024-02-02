# Iterative method
# Elements must be sorted for Binary search to work
def bsearch(array, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Recursive method
def rec_bsearch(list, low, high, target):
    if low <= high:
        midpoint = (low + high) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            return rec_bsearch(list, midpoint + 1, high, target)
        else:
            return rec_bsearch(list, 0, midpoint - 1, target)
    else:
        return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(rec_bsearch(nums, 0, len(nums) - 1, 8))
