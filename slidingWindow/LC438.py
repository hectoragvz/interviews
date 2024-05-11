# Find All Anagrams in a String


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    if len(p) > len(s):
        return []

    pDict = {}
    sDict = {}

    for i in range(len(p)):
        # Dict that contains the letts and their ocurrances in p
        pDict[p[i]] = 1 + pDict.get(p[i], 0)
        sDict[s[i]] = 1 + sDict.get(s[i], 0)  # Initialize the sDict

    res = [0] if pDict == sDict else []

    l = 0
    for r in range(len(p), len(s)):
        # Each new substring of size len(p)

        print(f"left: {s[l]}, Right:{s[r]}")
        print(s[r])
        sDict[s[r]] = 1 + sDict.get(s[r], 0)
        sDict[s[l]] -= 1

        if sDict[s[l]] == 0:
            sDict.pop(s[l])
        l += 1

        if sDict == pDict:
            res.append(l)

    return res


print(findAnagrams(s="cbaebabacd", p="abc"))
