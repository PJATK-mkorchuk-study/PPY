def deprecated(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"!!! {func.__name__} is deprecated, use {name} instead!!!")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@deprecated("goodAdd")
def badAdd(a, b):
    return a + b

@deprecated("awesomeFun")
def patheticFun(*, a, b):
    return a * b

c = badAdd(1, 7)
print(f"{c=}")

d = patheticFun(a=3, b=7)
print(f"{d=}")