# We look up the value we are looking for 1 by one

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
target = 13


def linear_search(arr, target):
  """
  Returns the index position of the target variable if found, else returns -1
  """
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1  
  
print(linear_search(nums, target))