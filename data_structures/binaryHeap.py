import heapq # follows min heap style

heap = []

# Adding the element while maintaining the properties of the heap
heapq.heappush(heap, 10)

print(heap)

heapq.heappush(heap, 1)

print(heap)

# Removing the smallest value and also delete it from heap, maintaining the properties of the heap

# Returns the deleted value, which is the smallest
heapq.heappop(heap)

print(heap)

heapq.heappop(heap)

print(heap)

# Convert the given list to binary heap

numbers = [1,2,3, 44, 42, 5,7,8,9]
heapq.heapify(numbers)
print(numbers)

# Push mentioned item and return the smalles value from the heap and deleting it
heapq.heappushpop(numbers, 89)
print(numbers)