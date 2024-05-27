# LC77 Combinations

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""


def combine(n, k):
    res = []

    def backtrack(start, comb):
        if len(comb) == k:
            res.append(comb[:])
            return

        for i in range(start, n + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()  # return up

    backtrack(1, [])
    return res


print(combine(n=4, k=2))
