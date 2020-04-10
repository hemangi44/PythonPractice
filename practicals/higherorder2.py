def combine_values(func, values):


    current = values[0]
    for i in range(1, len(values)):
        current = func(current, values[i])
    return current

def add(x, y):
    return x + y

# multiplication
def mul(x, y):
    return x*y

# adds all the values in the list
print(combine_values(add, [1,2,3,4] ))

# multiplies all the elements in the list
print(combine_values(mul, [1,2,3,4] ))