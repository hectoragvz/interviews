# Key - value mapping
# This creates an empty dictionary 
d = {}
d[1] = 'yes'
d['1'] = "no"
# These are different implementations of 1 and "1"
# key is transformed into a number, or ASCII in this case then into a memory location
print(d[1], d["1"])

d[2] = 9000
print(d[2])

# Instance of a class as a value
class my_class:
  def __init__(self):
    self.data = "data"

instance = my_class()
d['object'] = instance
print(d['object'].data)

# ITERATING
for key in d.keys():
  print(key) # keys

for key, value in d.items():
  print(key, value) # both key and value, returned as tuples

for value in d.values():
  print(value)

# Dictionaries do not represent any kind of order, contrary to arrays or Python lists