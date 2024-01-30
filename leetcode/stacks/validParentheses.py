def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pairs = {"]": "[", "}": "{", ")": "("}

    for i in range(len(s)):
        if s[i] in pairs.keys():
            if stack and stack[-1] == pairs[s[i]]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])

    return True if not stack else False
