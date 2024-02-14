import random

# " The worst-case Scenario for Quicksort occur when the pivot at each step consistently results in highly unbalanced partitions. When the array is already sorted and the pivot is always chosen as the smallest or largest element. To mitigate the worst-case Scenario, various techniques are used such as choosing a good pivot (e.g., median of three) and using Randomized algorithm (Randomized Quicksort ) to shuffle the element before sorting.  (GeeksforGeeks)"


# Placing the pivot
def pivot_place(list1, first, last):
    
    random_index = random.randint(first, last)

    list1[random_index], list1[first] = list1[first], list1[random_index]

    pivot = list1[first]
    left = first + 1
    right = last

    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if right < left:
            # indexes have crossed each other (pivot place found) break loop
            break
        else:

            list1[left], list1[right] = list1[right], list1[left]

    list1[first], list1[right] = list1[right], list1[first]

    return right


def quicksort(list1, first, last):
    if first < last:
        p = pivot_place(list1, first, last)
        quicksort(list1, first, p - 1)
        quicksort(list1, p + 1, last)


# main
list1 = [56, 26, 93, 17, 31, 44]
print(f"Original list: {list1}")
n = len(list1)
quicksort(list1, 0, n - 1)
print(f"Sorted list: {list1}")
