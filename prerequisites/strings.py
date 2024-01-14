# Strings are similar to lists
s = "abc"

# Strings are immutable
s += "def"
print(s)

# Valid numeric strings can be converted
print(int("123") + int("123"))

# and numbers can be converted to strings
print(str(123) + str(123))

# ASCII value
print(ord("a"))

# Combine a list of strings
strings = ["a", "b", "c"]
print("".join(strings))