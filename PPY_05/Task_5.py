def func(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] != lst[j]:
                yield (lst[i], lst[j])


pairs = func([1, 1, 3])

for pair in pairs:
    print(pair)
