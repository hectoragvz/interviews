import math


# KOKO eating bananas
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        k = (r + l) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res


print(minEatingSpeed(piles=[3, 6, 7, 11], h=8))
