#Single Inheritance
#Student
print("")
print("1]Enter the student name and age,roll_no")
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age =age

class student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

student = student("Mayuri",20,101)
print(student.name,student.age,student.roll_no)

#animal and dog
print("")
print("2]Animal and dog")
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def brak(self):
        print("Dog is barking")

Dog=Dog()
Dog.eat()
Dog.brak()

#vehical and car
print("")
print("3]vehical and car")
class vehical:
    def __init__(self,speed):
        self.speed=speed

class Car(vehical):
    def __init__(self, speed,fuel):
        super().__init__(speed)  
        self.fuel = fuel

C = Car(120,"petrol")
print(C.speed,C.fuel)    


#Account-savings Acconct
print("")
print("4]Account-savings Acconct")
class Account:
    def __init__(self, balance):
        self.balance = balance

class SavingAccount(Account):
            def interest(self):
                return self.balance*0.005
a = SavingAccount(10000)
print(a.interest())

#Emp,person, manager 
print("")
print("5]Emp,person, manager ")
class person:
     def __init__(self,name):
          self.name=name
class emp(person):
     def __init__(self, name,emp_id):
          super().__init__(name)
          self.emp_id= emp_id
class manager(emp):
     def __init__(self, name,emp_id,dept):
          super().__init__(name,emp_id)
          self.dept=dept

m= manager("Mayuri",201,"HR")
print(m.name,m.emp_id,m.dept)          

#Multilevel Inheritance
#device,mobile,smartphone
print("")
print("6]device,mobile,smartphone")
class device:
    def power(self):
         print("Power ON")

class mobile(device):
     def call(self):
          print("Calling")

class smartphone(mobile):
     def internet(self):
          print("internet access")

s=smartphone()
s.power()
s.call()
s.internet()

#Shape
print("")
print("7]shape,rectangle,cuboid")

class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


class Cuboid(Rectangle):
    def __init__(self, l, w, h):
        super().__init__(l, w)
        self.h = h

    def volume(self):
        return self.l * self.w * self.h
c = Cuboid(10, 5, 3)
print("Area of Rectangle:", c.area())
print("Volume of Cuboid:", c.volume())


#deparment company
print("")
print("8]deparment company")
class Company:
    def company_name(self):
        print("ABC Ltd")

class Department(Company):
    def dept_name(self):
        print("IT")

class Employee(Department):
    def emp_name(self):
        print("Suresh")

e = Employee()
e.company_name()
e.dept_name()
e.emp_name()

#Hierarchical Inheritance
print("")
print("9] Animal → Dog, Cat")
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()
 
print("")
print("10] Employee → Developer, Tester") 
class Employee:
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary: ₹50,000")

class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary: ₹40,000")

Developer().calculate_salary()
Tester().calculate_salary()

print("")
print("11] Shape → Circle, Square")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square Area:", self.side * self.side)

Circle(5).area()
Square(4).area()

print("")
print("12] Vehicle → Bike, Truck")
class Vehicle:
    def mileage(self):
        pass

class Bike(Vehicle):
    def mileage(self):
        print("Bike Mileage: 60 km/l")

class Truck(Vehicle):
    def mileage(self):
        print("Truck Mileage: 15 km/l")

Bike().mileage()
Truck().mileage()

#Multiple Inheritance
print("")
print("13] Father + Mother → Child")
class Father:
    def father_trait(self):
        print("Father: Strong")

class Mother:
    def mother_trait(self):
        print("Mother: Caring")

class Child(Father, Mother):
    def child_traits(self):
        self.father_trait()
        self.mother_trait()

Child().child_traits()

print("")
print("14] Camera + Phone → SmartDevice")
class Camera:
    def photo(self):
        print("Taking Photo")

class Phone:
    def call(self):
        print("Making Call")

class SmartDevice(Camera, Phone):
    pass

device = SmartDevice()
device.photo()
device.call()

print("")
print("15] Engine + Wheels → Car")
class Engine:
    def engine_type(self):
        print("Petrol Engine")

class Wheels:
    def wheel_count(self):
        print("4 Wheels")

class Car(Engine, Wheels):
    pass

car = Car()
car.engine_type()
car.wheel_count()

print("")
print("16] Writer + Editor → Author")
class Writer:
    def write(self):
        print("Writing content")

class Editor:
    def edit(self):
        print("Editing content")

class Author(Writer, Editor):
    pass

author = Author()
author.write()
author.edit()

#Hybrid Inheritance
print("")
print("17] Person → Employee → Manager (+ Intern)")
class Person:
    def show_person(self):
        print("I am a Person")

class Employee(Person):
    def show_employee(self):
        print("I am an Employee")

class Manager(Employee):
    def show_manager(self):
        print("I am a Manager")

class Intern(Employee):
    def show_intern(self):
        print("I am an Intern")

Manager().show_manager()
Intern().show_intern()

print("")
print("18] Animal → Mammal → Dog (+ Bat)")
class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def sound(self):
        print("Dog barks")

class Bat(Mammal):
    def fly(self):
        print("Bat flies")

Dog().sound()
Bat().fly()

print("")
print("19] Account → SavingsAccount (+ CurrentAccount, BusinessAccount)")
class Account:
    def account_type(self):
        print("Bank Account")

class SavingsAccount(Account):
    def interest(self):
        print("Savings Interest: 4%")

class CurrentAccount(Account):
    def overdraft(self):
        print("Overdraft Available")

class BusinessAccount(Account):
    def gst(self):
        print("GST Enabled")

SavingsAccount().interest()
CurrentAccount().overdraft()
BusinessAccount().gst()

print("")
print("20] School → Teacher → SubjectTeacher (+ Student)")
class School:
    def school_name(self):
        print("ABC School")

class Teacher(School):
    def teach(self):
        print("Teaching Students")

class SubjectTeacher(Teacher):
    def subject(self):
        print("Subject: Mathematics")

class Student(School):
    def learn(self):
        print("Learning Subjects")

SubjectTeacher().subject()
Student().learn()
