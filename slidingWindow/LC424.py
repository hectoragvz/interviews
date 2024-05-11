# Longest Repeating Character Replacement
def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    left = 0
    sDict = {}
    maxLen = 0

    for right in range(len(s)):
        sDict[s[right]] = 1 + sDict.get(s[right], 0)
        while (right - left + 1) - max(sDict.values()) > k:
            sDict[s[left]] -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)
    return maxLen


print(characterReplacement(s="AABABBA", k=1))
