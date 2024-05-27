# LC 78 Subsets


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    overallRes = []

    def backtrack(number, subset):
        if number == len(nums):
            overallRes.append(subset[:])
            return
        # Pick the number
        print("appending")
        subset.append(nums[number])
        backtrack(number + 1, subset)
        subset.pop()
        # Don´t pick
        print("skipping")
        backtrack(number + 1, subset)

    backtrack(0, [])
    return overallRes


print(subsets(nums=[1, 2, 3]))
