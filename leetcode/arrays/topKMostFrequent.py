def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        if n not in count.keys():
            count[n] = 1
        else:
            count[n] += 1

    for key, value in count.items():
        freq[value].append(key)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            


print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))