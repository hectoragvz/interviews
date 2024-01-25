def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_word = dict()
    t_word = dict()

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] not in s_word.keys():
            s_word[s[i]] = 1
        else:
            s_word[s[i]] += 1

    for j in range(len(t)):
        if t[j] not in t_word.keys():
            t_word[t[j]] = 1
        else:
            t_word[t[j]] += 1

    for k, v in s_word.items():
        if k not in t_word.keys():
            return False
        elif t_word[k] != v:
            return False
    return True


print(isAnagram("anagram", "nagaram"))