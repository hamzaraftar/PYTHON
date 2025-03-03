# class Employee:
#     def displa(self):
#         print("this is employee class")

# class Manager(Employee):
#     def show(self):
#         print("this is manager class ")

#  Hierarchical Inheritance

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age =  age
    def display(self):
        print('This peron ')

class Employee(Person):
    def __init__(self, sal ):
        self.sal =sal
        def display(self):
            print('This Employee ')

class Student(Person):
    def __init__(self, name, age , marks):
        super().__init__(name, age)
        self.marks = marks

        def display(self):
            print('This Student ')

s1 = Student('hamza', 12 , 333)
print(s1.age)