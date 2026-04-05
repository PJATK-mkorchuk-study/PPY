def func(lst):
    for i in range(0, len(lst), 2):
        yield tuple(lst[i:i+2])

lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 4, 5]

print("Lst 1:")
for pair in func(lst_1):
    print(pair)

print("\nLst 2:")
for pair in func(lst_2):
    print(pair)