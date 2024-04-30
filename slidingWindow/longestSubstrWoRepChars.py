def lengthOfLongestSubstring(s):

    left = 0
    maxLen = 0
    test = set()

    for right in range(len(s)):
        while s[right] in test:
            test.remove(s[left])
            left += 1
        test.add(s[right])
        maxLen = max(maxLen, len(test))
    return maxLen


print(lengthOfLongestSubstring("bbbbb"))
