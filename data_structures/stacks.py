# Implementing a stack with python via lists
# LIFO Approach

# Push ---> append
# Pop ---> pop

stack = []

print(f"original stack: {stack}")

stack.append(10) # Append at last
stack.append(20)
stack.append(30)

print(f"After pushing(appending) to stack: {stack}")

stack.pop() # removes the last element from the stack
stack.pop()
stack.pop()


print(f"After popping from stack: {stack}")

# IS empty?
len(stack) == 0 # returns true or false

stack.append(10) # Append at last
stack.append(20)
stack.append(30)

# Checking last element
print(stack[-1])
print(stack[len(stack) - 1])

