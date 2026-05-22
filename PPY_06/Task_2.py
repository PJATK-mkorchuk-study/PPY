def repeat(n):
    def decorator(function):
        def newFunc(*args, **kargs):
            for i in range(n):
                function(*args, **kargs)
        return newFunc
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello { name }")

print(greet("Max"))