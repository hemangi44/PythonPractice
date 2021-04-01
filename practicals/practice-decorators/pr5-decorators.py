class employee:
	emp_count = 0                   #static variable/class variable
	def __init__(self, eid, ename, esalary):
		self.eid = eid
		self.ename = ename
		self.esalary = esalary
	def info(self):
		print("id ", self.eid)
		print("name ", self.ename)
		print("salary ", self.esalary)
	@staticmethod
	def show_ecount():
		print("count = ", employee.emp_count)

emp_data = []
while True:
    op = int(input("1 add, 2 view, 3 view emp count, 4 remove and 5 exit "))
    if op == 1:
        eid=int(input("enter employee id :"))
        ename=input("enter employee name ")
        esalary=float(input("enter employee salary "))
        e=employee(eid,ename,esalary)
        emp_data.append(e)
        print("employee added")
        employee.emp_count = employee.emp_count + 1
    elif op == 2:
        for e in emp_data:
            e.info()
    elif op == 3:
        employee.show_ecount()
    elif op == 4:
        reid=int(input("enter eid to remove"))
        found = False
        for e in emp_data:
            if e.eid==reid:
                emp_data.remove(e)
                print("employee removed")
                found=True
        if not found:   
             print("employee does not exist")
    elif op == 5:
        break
    else:
        print("invalid option")

