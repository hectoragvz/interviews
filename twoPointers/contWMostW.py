def maxArea(height):
    res = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # The distance between the 2 poles
        distance = right - left
        smallest = min(height[left], height[right])
        # Calculate current area and compare
        currArea = distance * smallest
        res = max(currArea, res)
        # Which should we move? the smalles to keep looking
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return res


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
