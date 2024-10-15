class student:
	branch="CSE";
	def a(self,rollno,name):
		self.rollno=rollno;
		self.name=name;
	def display(self):
		print(self.rollno)
		print(self.name)
		print(student.branch)
s = student()
s.a(1,"deepak")
s.display()
