num=int(input("Enter the number of rows:"))
if num<0:
	print("Enter a positive number")
else:
    for i in range(0,num):
        for j in range(0,num-i-1):
            print("",end="-")
        for j in range(0,i+1,1):
            print(chr(num-i-1+97), end=" ")
        for j in range(0,num-i-1,2):
            print("",end="-")
        print()
    
  