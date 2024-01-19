# Lookup notation by index = O(1) - nums[9] = x

# Lookup by value = O(n)

# Array traversal = O(n)

# Array insertion = O(n)

# Array deletion = O(n)

# In PYTHON, lists are implemented as DYNAMIC ARRAYS

# Some exercises
month_expenses = [2200, 2350, 2600, 2130, 2190, 1950]

print(month_expenses[1] - month_expenses[0])

total = 0
for month in range(3):
  total += month_expenses[month]
print(total)