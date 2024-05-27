# Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


def permute(nums):

    res = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res


print(permute(nums=[1, 2, 3]))
