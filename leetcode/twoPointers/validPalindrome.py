class Solution(object):

    def isAlphaNum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") 
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not self.isAlphaNum(s[left]):
                left += 1
            elif not self.isAlphaNum(s[right]):
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True