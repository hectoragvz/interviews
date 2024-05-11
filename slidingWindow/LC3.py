# Longest Substring withour Repeating Character


def lengthOfLongestSubstring(s):
    maxLen = 0
    left = 0
    sDict = {}

    for right in range(len(s)):
        sDict[s[right]] = 1 + sDict.get(s[right], 0)
        while max(sDict.values()) != 1:
            sDict[s[left]] -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)
    return maxLen


print(lengthOfLongestSubstring(s="pwwkew"))

# MORE OPTIMAL HERE

""" def lengthOfLongestSubstring(self, s):
        maxLen = 0
        left = 0
        sSet = set()

        for right in range(len(s)):
            while s[right] in sSet:
                sSet.remove(s[left])
                left += 1
            sSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen """
