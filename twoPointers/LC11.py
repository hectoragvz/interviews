# Container with most water
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxCap = 0
    left = 0
    right = len(height) - 1

    while left < right:
        capacity = min(height[left], height[right]) * (right - left)
        maxCap = max(maxCap, capacity)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxCap


print(maxArea(height=[1, 1]))
