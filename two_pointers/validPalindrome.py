def isPalindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:
        if not isValid(s[left]):
            left += 1
        elif not isValid(s[right]):
            right -= 1
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


def isValid(char):
    return (
        ord("A") <= ord(char) <= ord("Z")
        or ord("a") <= ord(char) <= ord("z")
        or ord("0") <= ord(char) <= ord("9")
    )


print(isPalindrome("A man, a plan, a canal: Panama"))
