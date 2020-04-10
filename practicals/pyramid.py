num=int(input("Enter the number of rows:"))
if num<0:
	print("Enter a positive number")
else:
    for i in range(0,num):
        for j in range(0,num-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print("*", end=" ")
        print()
        
#first for loop is for number of rows
#second for loop is for printing space in each row
#third for loop is for printing star