def type_check(function):
    def newFunc(*args, **kargs):
        try:
            return int(args[0]) + int(args[1]) + int(args[2])
        except ValueError:
            raise TypeError("All number should be integers")
    return newFunc

@type_check
def sum_all(a, b, c):
    return a + b + c

print(sum_all(1, "a", 3))