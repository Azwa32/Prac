#Includes inheritance with parent/child classes

"""
Create a Person class with the following attributes:

name
age
gender
height
weight
Create a Student subclass of Person with the additional attributes:

student_id
major
gpa
Create a Teacher subclass of Person with the additional attributes:

teacher_id
subject
salary
For each class, create an __init__ method that initializes the attributes, as well as a display method that prints out all the attributes for the object.

Create at least one instance of each class and call their display method to make sure everything is working correctly.
"""

class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def display(self):
        print(f"{self.name} {self.age} {self.gender} {self.height} {self.weight}")

class Student(Person):
    def __init__(self, name, age, gender, height, weight, student_id, major, gpa):
        super().__init__(name, age, gender, height, weight)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    def display(self):
        print(f"{self.name} {self.age} {self.gender} {self.height} {self.weight} {self.student_id} {self.major} {self.gpa}")

class Teacher(Person):
    def __init__(self, name, age, gender, height, weight, teacher_id, subject, salary):
        super().__init__(name, age, gender, height, weight)
        self.teacher_id = teacher_id
        self.subject = subject
        self.salary = salary

    def display(self):
        print(f"{self.name} {self.age} {self.gender} {self.height} {self.weight} {self.teacher_id} {self.subject} {self.salary}")


Jeremy = Person("Jeremy Clarkson", 134, "male", 234, 100)
James = Teacher("James May", 83, "female", 232, 100, 1234567, "advanced triganometry", 100)
Richard = Student("Richard Hamond", 29, "male", 100, 32, 1234568, "physics", 200)

Jeremy.display()
James.display()
Richard.display()



