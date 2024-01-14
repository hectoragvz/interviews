# Functions
def myFunc(m, n):
    return m + n


# Nested funcitons
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner


print(outer("a", "b"))


def double(arr, val):
    def helper():
        # Mod arrays works
        for i, n in enumerate(arr):
            arr[i] *= 2
        # will only mod val in helper scope
        # vale *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3

double(nums, val)
