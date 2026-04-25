def lengthOfLongestSubstring(s):
    left = 0
    maxAns = 0
    seens = set()

    for right in range(len(s)):
        while s[right] in seens:
            seens.remove(s[left])
            left += 1
        seens.add(s[right])

        maxAns = max(right - left + 1, maxAns)

    return maxAns


print(lengthOfLongestSubstring("pwwkew"))
