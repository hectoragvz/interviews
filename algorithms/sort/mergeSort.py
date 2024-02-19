# Divide the list until we get single-element lists
# Compare each single-list element and merge them sorted


def merge_sort(list1):

  # Base case to check for single-element list
  if len(list1) > 1:

    # Find the middle point
    mid = len(list1) // 2

    # Dividing the list
    left = list1[:mid]
    right = list1[mid:]

    # Recursively dividing the lists
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i<len(left) and j<len(right):
      if left[i] < right[j]:
        list1[k] = left[i]
        i+=1
        k+=1
      else:
        list1[k] = right[j]
        j+=1
        k+=1
    while i < len(left):
      list1[k] = left[i]
      i+=1
      k+=1
    while j < len(right):
      list1[k] = right[j]
      j+=1
      k+=1


list = [2,5,8,2,7,55,32,88,5,1]
merge_sort(list)
print(list)