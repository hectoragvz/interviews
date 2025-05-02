# Must not have any problems implementing binarySearch from scratch


def searchBinary(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (right + left) // 2
        if numbers[mid] > target:
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            return mid
    return "Not Found"


print(searchBinary(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=3))
