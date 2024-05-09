def countGoodSubstrings(s):
    if len(s) < 3:
        return 0
    res = 0
    firstSub = s[:3]
    sDict = {}
    for i in range(len(firstSub)):
        sDict[firstSub[i]] = 1 + sDict.get(firstSub[i], 0)
    if max(sDict.values()) == 1:
        res += 1
    left = 0
    for right in range(3, len(s)):
        print(s[right])
        # print(f"Adding: {s[right]}, subtracting: {s[left]}")
        # Adding right char
        sDict[s[right]] = 1 + sDict.get(s[right], 0)
        # Subtracting left
        sDict[s[left]] -= 1
        # Is there an element with a value of 0? Remove it if yes
        if sDict[s[left]] == 0:
            sDict.pop(s[left])
        # Is there any value appearing more than once, if there is skip it
        if max(sDict.values()) == 1:
            res += 1
        left += 1
    return res


print(countGoodSubstrings(s="aababcabc"))
