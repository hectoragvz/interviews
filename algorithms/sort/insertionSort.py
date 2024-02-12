# Just know insertion sort and itz runtime and how it works

def insertion_sort(a):
  for i in range(1, len(a)): # starts at second element
    current = a[i] # index of unsorted part
    pos = i
    while current < a[pos - 1] and pos > 0:
      a[pos] = a[pos-1]
      pos = pos-1
    a[pos] = current


b = [4,5,7,8,9,2]
insertion_sort(b)
print(b)