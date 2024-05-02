def quicksort(arr, left, right):
    if left < right:  # Contains at least two elements
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:  # Havent crossed
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i < j:
            # Havne´t crossed
            arr[i], arr[j] = arr[j], arr[i]
    # They have crossed
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


arr1 = [7, 4, 0, 12, 3, 7, 99]
quicksort(arr1, 0, len(arr1) - 1)
print(arr1)
