def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def util(func,x,y):
    return func(x,y)
    
print(util(x=4,y=5,func=add))
print(util(x=2,y=5,func=mul))
