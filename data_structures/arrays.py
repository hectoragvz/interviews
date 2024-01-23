# Lookup notation by index = O(1) - nums[9] = x

# Lookup by value = O(n)

# Array traversal = O(n)

# Array insertion = O(n)

# Array deletion = O(n)

# In PYTHON, lists are implemented as DYNAMIC ARRAYS

# Some exercises
new_list = [1,2,3]
result = new_list[2] #search by index element of the array O(1)

# Searching for a value O(n)
if 1 in new_list:
  print(True)

for n in range(len(new_list)):
  if new_list[n] == 1:
    print(True)
    break

for x in new_list:
  if x == 1:
    print(True)
    break

numbers = []
numbers.append(1) # Append at the end
numbers.insert(0,1) # Insert at beginning (index, value)
numbers.extend([1,2,3]) # appends list at the end
numbers.remove(2)
print(numbers)