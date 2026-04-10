class Solution:
    def encode(self, strs):
        sol = ""
        for word in strs:
            sol += str(len(word))
            sol += "#"
            sol += word
        return sol

    def decode(self, s):
        sol = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            length = s[i:j]
            sol.append(s[j + 1 : j + 1 + int(length)])
            i = j + 1 + int(length)
        return sol
