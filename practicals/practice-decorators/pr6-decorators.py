# any object which implements the special __call__() method is termed callable
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("cannot divide with 0!")
            return

        return func(a, b)

    return inner


def divide():
    print(a / b)


new_divide = smart_divide(divide)
new_divide(5, 0)

## Above wrapper statement is equivalient of below decorator


@smart_divide
def divide(a, b):
    print(a / b)


divide(5, 0)
