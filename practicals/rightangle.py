num=int(input("Enter the number of rows:"))
if num<0:
	print("Enter a positive number")
else:
    for i in range(num,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()

#first for loop is print the rows
#second for loop is for printing the columns