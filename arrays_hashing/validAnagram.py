def isAnagram(s, t):
    sMap, tMap = {}, {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        # Both are assured to have the same length
        # Constructs the 2 dictionaries with the letters and frequencies
        sMap[s[i]] = sMap.get(s[i], 0) + 1
        tMap[t[i]] = tMap.get(t[i], 0) + 1

    return tMap == sMap


print(isAnagram(s = "rat", t = "car"))
