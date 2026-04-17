def validPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and (s[left] == " " or not s[left].isalnum()):
            left += 1
        while left < right and (s[right] == " " or not s[right].isalnum()):
            right -= 1
        # We are a both not space char
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


print(validPalindrome("A man, a plan, a canal: Panama"))
