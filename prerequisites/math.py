# Divisions is decimal by default
print(5 / 2)  # 2.5

# // rounds dows
print(5 // 2)  # 2

# CAUTION
# negatie numbers will round down as well
print(-3 // 2)  # -2

# A workoround for rounding towards zero is to use decimal division and then convert to int
print(int(-3 / 2))  # -1

# Modding is similar to most langs
print(10 % 3)  # 1

# Except for negative values
print(-10 % 3)  # 2

# Workaround
import math

print(math.fmod(-10 % 3))  # -1

# Some extra mth helpers
import math

print(math.floor((3 / 2)))  # round down
print(math.ceil(3 / 2))  # round up
print(math.sqrt(2))  # sqrt
print(math.pow(2, 3))  # to the power

# Max, min int
# Literally infinity
float("inf")
float("-inf")