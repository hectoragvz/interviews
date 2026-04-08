def topKFrequent(nums, k):
    # Create a freq dictionary
    sol = []
    seens = {}
    for num in nums:
        seens[num] = seens.get(num, 0) + 1
    freqs = {}
    for num in range(len(nums), 0, -1):
        freqs[num] = []
    for key, value in seens.items():
        freqs[value].append(key)

    for key, value in freqs.items():
        if value:  # Is there even a number that many times?
            for val in value:
                sol.append(val)
                if len(sol) == k:
                    return sol


print(topKFrequent([1, 1, 1, 2, 2, 3], k=2))
