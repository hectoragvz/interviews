# Search a 2D matrix
def searchMatrix(matrix, target):
    # In what row is the number we look for
    left, right = 0, len(matrix) - 1
    while left <= right:
        mid = (right + left) // 2
        if target < matrix[mid][0]:
            # is in the first row
            right = mid - 1
        elif target > matrix[mid][-1]:
            # target is in the last row
            left = mid + 1
        else:
            break  # target is in that row
    # WE must look between the top and bottom
    start, end = 0, len(matrix[mid]) - 1
    while start <= end:
        midpoint = (end + start) // 2
        if matrix[mid][midpoint] == target:
            return True
        elif matrix[mid][midpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint - 1
    return False


print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=8))
