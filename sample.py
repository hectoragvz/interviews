def isPalindrome(word):
    def isaplhaNum(c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    left = 0
    right = len(word) - 1

    while left < right:
        while left < right and not isaplhaNum(word[left]):
            left += 1
        while right > left and not isaplhaNum(word[right]):
            right -= 1
        if word[left].lower() != word[right].lower():
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("race a car"))
