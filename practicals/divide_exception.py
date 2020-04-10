def divq(num):
    if num==0:
        raise Exception("Don\'t enter zero")
    pass
    pass
    return 100/num

num=int(input('enter a number'))
try:
     print(divq(num))
     print("helooooooooooo")
     print("booooooo")
except:
    print('exception catch')