class student: 
	prof_name="Kamal Sir"
	def __init__(self,r,n,m):
		self.rno=r
		self.name=n
		self.marks=m
	def talk(self):
		print("rno =",self.rno)
		print("name =",self.name)
		print("marks =",self.marks)
	def find_grade(self):
		if self.marks>80:
			print("Grade A")
		else:
			print("Grade B")
	@staticmethod
	def get_prof_name():
		print("professor name=",student.prof_name)

rno=int(input("enter rno "))
name=input("enter name ")
marks=int(input("enter marks "))

s1=student(rno,name,marks)
s1.talk()
s1.find_grade()
s1.get_prof_name()
student.get_prof_name()