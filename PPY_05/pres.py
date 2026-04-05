def f(s, e):
    while s < e:
        return s
        s += 1


def g(s, e):
    while s < e:
        yield s
        print()
        s += 1

v = f(4, 6)
v2 = g(4, 6)

for el in v2:
    print(el)