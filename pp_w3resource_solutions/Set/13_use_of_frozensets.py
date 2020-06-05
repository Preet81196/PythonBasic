x = frozenset([1, 2,3])
y = frozenset([3, 4, 5, 6, 7])

print(x.isdisjoint(y))

print(x.difference(y))

print(x.union(y))
