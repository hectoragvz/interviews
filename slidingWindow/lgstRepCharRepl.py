def characterReplacement(s, k):
    diffs = {}
    res = float("-inf")
    left = 0
    maxFreq = 0

    for right in range(len(s)):
        diffs[s[right]] = diffs.get(s[right], 0) + 1

        # Update the most common element
        maxFreq = max(maxFreq, diffs[s[right]])

        while (right - left + 1) - maxFreq > k:
            diffs[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    return res


print(characterReplacement("AABABBA", 1))
