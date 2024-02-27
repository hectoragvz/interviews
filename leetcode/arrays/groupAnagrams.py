from collections import defaultdict 

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagrams = defaultdict(list)

    for word in strs:
        count = [0] * 26 # a ... z
        
        for char in word:
            count[ord(char) - ord("a")] += 1 # Replaces the 0s of the count with a values for each existing letter

        anagrams[tuple(count)].append(word)

    return anagrams.values()
                     


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))