n=int(input("Enter the number of rows:"))
if n<0:
	print("Enter a positive number")
else:
	for i in range(1,n+1,2):
		for j in range(1,i+1):
			print("*",end= " ")
		print()