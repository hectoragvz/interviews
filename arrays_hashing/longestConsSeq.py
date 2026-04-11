def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            curr = 1
            while (num + curr) in numSet:
                curr += 1
            longest = max(longest, curr)
    return longest


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
