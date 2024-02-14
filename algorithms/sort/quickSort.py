# Placing the pivot
def pivot_place(list1, first, last):

  # Taking the pivot as the first element in the array
  # pivot = list[last] if you want to take the last element
  # left = first
  # right = last - 1

  pivot = list1[first]
  left = first + 1
  right = last

 # Change the < and > symbols
  while True:
    while left <= right and list1[left] <= pivot:
      left += 1
    while left <= right and list1[right] >= pivot:
      right -= 1
    if right < left: 
      # indexes have crossed each other (pivot place found) break loop
      break
    else:
      # Swap the list values corresponding to the indexes
      list1[left], list1[right] = list1[right], list1[left]

  # Since the first element is selected as pivot, swap with right
  # Change right to left and first to last for last element
  list1[first], list1[right] = list1[right], list1[first]

  # returns the index of the pivot in the correct order in the list
  # return left for last element taken
  return right

# Divide the list
def quicksort(list1, first, last):
  if first < last:
    p = pivot_place(list1, first, last)
    quicksort(list1, first, p-1)
    quicksort(list1, p+1, last)
  

#main
list1 = [56, 26, 93, 17, 31, 44]
print(f"Original list: {list1}")
n = len(list1)
quicksort(list1, 0, n-1)
print(f"Sorted list: {list1}")

