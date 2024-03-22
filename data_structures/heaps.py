import heapq

# A heap is an implementation of a priority queue
"""
ith element = list[i]
left child = (2*i)+1
right child = (2*1)+2
parent = (i-1)//2
"""

# Min heap by default
data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
data = [-x for x in data] # Easy way to turn into a max heap

heapq.heapify(data)
print(f"Heap: {data}")

# Popping the element with the highest priority
print(f"Removing the highest priority element which is: {heapq.heappop(data)}...")  # -> 1

print(f"Heap after deletion: {data}")

number = 2
print(f"Adding {number} to the heap...")
heapq.heappush(data, 2)  # Adding an element to the heap

print(f"Heap after addition: {data}")
