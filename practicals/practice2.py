class Employee:
    def __init__(self,name,age,emp_id):
        self.name=name
        self.age=age
        self.emp_id=emp_id
    
    def getname(self):
        return self.name
    
    def getage(self):
        return self.age
    
    def getemp_id(self):
        return self.emp_id

emp1=Employee("BIPIN",35,1)
emp2=Employee("HEMANGI",25,2)

print(emp1.getname(),emp1.getage())
print(emp2.getname())

emp1=emp2
print(emp1.getname(),emp1.getage())