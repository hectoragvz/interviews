def isValid(s):
    test = []
    pairs = {"}": "{", "]": "[", ")": "("}
    for par in s:
        if par in pairs:
            if not test or test[-1] != pairs[par]:
                return False
            test.pop()
        else:
            test.append(par)

    return not test


print(isValid("(]"))
