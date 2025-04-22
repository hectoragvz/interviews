## Review from Neetcode video

Python is a dynamically typed language. Types are determined at runtime.

You can also do multiple assignments.

Incrementing works n+=1 and not n++.

None is null

If statements don´t need () parentheses or {} curly brackets.

Parentheses are need for multi-line comments.

Looping from i=0 to i=4 - for i in range(5) five is not inclusive

2 to 5 - for i in range(2, 5) si it is basically (start inclusice, stop not inclusive)

For loops in the end are (start, stop, step) - inclusive, not inclusive, step

Division is decimal by default

print(5/2) - 2.5

print(5//2) - rounds down

### Arrays

Are called lists in python

arr = [1,2,3,4]

Can be used as a stack ||

arr.append(4) push at the end

arr.pop() - removes from the end

arr.insert(1,7) - inserts a 7 at index 1 - big 0 of n

Initialize array of size n with default value to 1

n = 5
arr = [1] + n
print(len(arr))
print(arr[-1]) - last element
print(arr[1:3]) from value 1 to 2 since :not inclusive

a, b, c, = [1,2,3] - Unpacking

for i in range(len(nums)) - with index
print(nums[i])

for n in nums: without index

for i, n in enumarate(nums): index and number
if you do zip(arr1, arr2) and print, you will get pais for each number of the different arrays

Reversing an array nums.reverse()

Sorting an array nums.sort() / reverse=true as an argument perhaps

### List Comprehension

arr = [i for i in range(5)]
[0, 1, 2, 3, 4]

arr = [[0]\*4 for i in range(4)] - 4x4 of all 0s

#### Strings

Strings are like arrays

s = "abc"
prnt(s[0:2])

Strings can be converted to strings and backwards

ASCI value of a - ord('a')

strings = ["a", "b", "c"]
print("",.join(strings))

#### Queues =

from collections import deque - double ended by default

queue = deque()

queue.append(1)

queue.popleft() - constant time

queue.appendleft(n)

#### Hash Sets

mySet = set() - search in constant and insert in constant
can not containf duplicates

1 in mySet - true or false that easy

set([1,2,3])

#### Hash Maps

myMap = {}

myMap['Alice'] = 1
print(len(myMap))

Can reassign value

'Alice'in myMap

myMap.pop('Alice')

Looping through a map

for key in myMap: iterates though the keys

for val in myMap.values() - through the values

for key, val in myMap.items() - gives us both

#### Tuples

tup = (1,2,3)

Lists can not be keys for hashmaps

#### Functions

def myFunc(m, n):

#### Classes

class MyClass:

    def __init__(self, x, y...) # Constructor

        self.nums = nums

        self.size = len(nums)

    def get_length(self):
        return self.size
