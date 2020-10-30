N = 3
subsets = set()
subsets.add(frozenset())

for i in range(1, N + 1):
    new_subsets = set()
    for subset in subsets:
        nonfrz = set(subset)
        nonfrz.add(i)
        fz = frozenset(nonfrz)
        new_subsets.add(fz)
    subsets.update(new_subsets)

print(subsets)
