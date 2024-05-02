# Divide the list until we get single-element lists
# Compare each single-list element and merge them sorted


def merge_sort(arr):
    if len(arr) > 1:
        # Divide into two lists
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]
        merge_sort(left_arr)
        merge_sort(right_arr)
        # Merge step - we will compare two arrays by i (left most elem of first array) and j (left most elem of second array)
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        # Already transfered the elems from the right array to the merge array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        # Already transfered the elems from the left array to the merge array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


list = [2, 5, 8, 2, 7, 55, 32, 88, 5, 1]
print(merge_sort(list))
