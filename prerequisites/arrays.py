# https://www.w3schools.com/python/python_ref_list.asp
# Arrays are also called lists in python
arr = [1, 2, 3]
print(arr)

# can be used as stack
arr.append(4)  # inserts at the end
arr.append(5)  # inserts at the end
print(arr)

arr.pop()  # removes last element default but removes the element at the specified position
print(arr)

arr.insert(1, 7)  # inserts at index 1 a 7
print(arr)


# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n

# -1 is not out of bounds but the last value
arr = [1, 2, 3]
print(arr[-1])  # 3

# SUblists or slicing
arr = [1, 2, 3, 4]
print(arr[1:3])  # last not inclusive


# Unpacking
a, b, c = [1, 2, 3]  # vars must match the amount of values

# using index
nums = [1, 2, 3]
for i in nums:
    print(nums[1])

# without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Looping through multiple arrays simultaneously with unpacking
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()

# Sorting
nums.sort()  # Asc by default
arr.sort(reverse=True)  # Desc

# Custom sort by length
arr = ["Alice", "Bob", "Charly"]
arr.sort(key=lambda x: len(x))

# List comprehension
arr = [i for i in range(5)]
arr = [i+i for i in range(5)]

# 2D lists
arr2d = [[0] * 4 for i in range(4)]
print(arr2d)