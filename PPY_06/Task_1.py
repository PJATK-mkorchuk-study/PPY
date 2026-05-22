def uppercase(function):
    def newFunction(*args, **kargs):
        return args[0].upper()
    return newFunction

@uppercase
def func(a):
    return a

input = input("Enter a text: ")
print(func(input))
