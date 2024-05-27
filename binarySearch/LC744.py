# Find smallest letter greater than target

"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
"""


def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1

    while left <= right:
        mid = (left + right) // 2

        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # Element not in the array
    return letters[left] if left < len(letters) else letters[0]


print(nextGreatestLetter(letters=["c", "f", "j"], target="c"))
