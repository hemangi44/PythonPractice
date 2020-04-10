num=int(input("Enter a number"))
if num<0:
	print("Enter a positive number")

else:
    result=1
    for i in range(1,num+1,1):
        result=result*i
    print("The factorial of", num ,"is:", result)