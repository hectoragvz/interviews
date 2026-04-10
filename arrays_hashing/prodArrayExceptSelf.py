def productExceptSelf(nums):
    sol = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        sol[i] = prefix
        prefix = prefix * nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):  # Reverse order
        sol[i] = sol[i] * suffix
        suffix = suffix * nums[i]

    return sol


print(productExceptSelf([1, 2, 3, 4]))
