from itertools import combinations


class Apriori(object):
    def __init__(self, T, support):
        self.T = T
        self.support = support

    def generate_unique_items(self):
        unique_items = set()
        [unique_items.add(item) for ti in self.T for item in ti]
        return unique_items

    def count(self, d={}):
        for k, v in d.items():
            if v < self.support:
                del d[k]
            else:
                pass
        return d

    def findsubsets(self, S, m):
        return set(combinations(S, m))

    def generate_item_sets(self):
        itemset = self.generate_unique_items()
        d = dict()
        for i in range(1, len(itemset)):
            d[i] = dict()
            spec = dict()
            for ti in self.T:
                for s in self.findsubsets(itemset, i):
                    if s:
                        if set(s).difference(ti):
                            pass
                        else:
                            if spec.has_key(repr(s)):
                                spec[repr(s)] += 1
                            else:
                                spec[repr(s)] = 1

            d[i] = spec
        return d

    def display_results(self):
        res = self.generate_item_sets()
        for k, v in res.items():
            for k2, v2 in v.items():
                if v2 < self.support:
                    del res[int(k)][str(k2)]

        for r in res.values():
            if r:
                print r


if __name__ == '__main__':
    T = [['A', 'C', 'D'], ['B', 'D'], ['A', 'B', 'C', 'E'], ['B', 'D']]  # list of list containing the transactions
    min_support = 2
    apriori = Apriori(T, 2)
    apriori.display_results()
