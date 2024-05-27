# Find peak element

"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""


def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        # left neighbor greater
        if mid > 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
        # Right greater
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            return mid


print(findPeakElement(nums=[1, 2, 3, 1]))
