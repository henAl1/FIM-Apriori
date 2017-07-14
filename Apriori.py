from itertools import combinations

T = []  # list of list containing the transactions
itemset = set()
[itemset.add(item) for ti in T for item in ti]


def findsubsets(S, m):
    return set(combinations(S, m))


d = dict()

for i in range(1, len(itemset)):
    for s in findsubsets(itemset, i):
        for si in s:
            for ti in T:
                for ele in ti:
                    if si == ele:
                        if d.has_key(s):
                            d[s] += 1
                        else:
                            d[s] = 1
                    else:
                        pass
