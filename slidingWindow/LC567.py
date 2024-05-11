# Permutation in a String


def checkInclusion(s1, s2):
    s1Dict = {}
    s2Dict = {}

    for i in range(len(s1)):
        s1Dict[s1[i]] = 1 + s1Dict.get(s1[i], 0)
        s2Dict[s2[i]] = 1 + s2Dict.get(s2[i], 0)

    if s1Dict == s2Dict:
        return True
    # Got now initial dicts of len s1

    left = 0
    for right in range(len(s1), len(s2)):
        # Adding the right element
        s2Dict[s2[right]] = 1 + s2Dict.get(s2[right], 0)
        # Removing the left element
        s2Dict[s2[left]] -= 1

        # iS there a key with a 0?
        if s2Dict[s2[left]] == 0:
            s2Dict.pop(s2[left])

        if s1Dict == s2Dict:
            return True

        # Continue moving right
        left += 1

    return False


print(checkInclusion(s1="ab", s2="eidboaoo"))
