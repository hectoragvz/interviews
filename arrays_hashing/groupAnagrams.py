def groupAnagrams(strs):
    sol = []
    seens = {}

    for word in strs:
        # Create dummy dict for each word
        # tempDict = {}
        # for i in range(len(word)):
        #    tempDict[word[i]] = tempDict.get(word[i], 0) + 1
        wordSorted = "".join(sorted(word))  # Returns a key
        # print(wordSorted)
        # We now have a dictionary for the word
        # Check if the word´s dict is in the main dict
        if wordSorted in seens:
            # If it is, append the word to that dict key
            seens[wordSorted].append(word)
        else:
            # If not create that array and append to it
            seens[wordSorted] = [word]

    # ATM, we have arrays as values
    for arr in seens.values():
        sol.append(arr)

    return sol


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
