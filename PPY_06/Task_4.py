import datetime


def withDebug(function):
    def newFunc(*args, **kargs):
        if "DEBUG" in kargs:
            kargs.pop('DEBUG')

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp}: calling adder")
            print(f"args=({args}), kwargs=({kargs})")
            result = function(*args, **kargs)
            print(f"Result returned={result}\n")
            return result
        else:
            return function(*args, **kargs)
    return newFunc


@withDebug
def adder(a, b):
    return a + b


adder(1, 2, DEBUG="Yes")
print("no debug:", adder(3, 4))
adder(5, 6, DEBUG=True)