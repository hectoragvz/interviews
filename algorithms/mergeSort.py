# Implementing merge sort in an array
def merge_sort(list):
    """
    Sort the list in ASC order
    returns a new sorted list
    1. Divide and find the midpoint of the list into sublists
    2. Recursively sort the sublists created in step 1
    3. Combine the sorted sublists created in step 2
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide unsorted list at midpoint into sublists
    returns two sublist - left and right
    """

    mid = len(list) // 2
    left = list[:mid]  # Midpoint exclusive
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists or arrays sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
     return True
    
    return list[0] <= list[1] and verify_sorted(list[1:])

alist = [54, 23, 65, 7, 65, 25, 19]
l = merge_sort(alist)
print(verify_sorted(l))