def characterReplacement(s, k):

    left = 0
    res = 0
    count = {}

    for r in range(len(s)):

        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, r - left + 1)

    return res


print(characterReplacement(s="AABABBA", k=1))
