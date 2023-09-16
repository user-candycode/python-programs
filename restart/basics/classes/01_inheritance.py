class Person:
	def __init__(self,name,age):
	self._name = name
	self._age = age

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,value):
		if value < 1 or value > 120:
			raise ValueError("Age must be between 1 and 120")
		self._age = value

class Student(Person):
	def __init__(self,name,age):
		super().__init__(name,age)
		self.grade = []

	def add_grade(self,grade):
		self._grades.append(grade)
