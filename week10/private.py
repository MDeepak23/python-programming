class student:
	branch="CSE";
	def a(self,rollno,name):
		self.__rollno=rollno;
		self.__name=name;
	def display(self):
		print(self.__rollno)
		print(self.__name)
		print(student.branch)
s = student()
s.a(1,"deepak")
s.display()

