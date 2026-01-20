class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sort(self):
            print(f"My name is {self.name} and I am {self.age} years old.")

s1 = student("mayuri",20)
s1.sort()         


#task__2

class car:
     def __init__(self,brand,model):
          self.brand = brand
          self.model = model

#create 2 object
c1=car("honda","civic")
c2=car("honda","civic")

print("c1",c1.brand,c1.model) 
print("c2",c2.brand,c2.model)         
          

#task_3

class Book:
    def __init__(self,Tital,author):
        self.Tital = Tital
        self.author = author

    def index(self):
            print(f"tital name is {self.Tital} and I am {self.author} of this book.")

m1=Book("harry potter","jon")
m1.index()


 #task_4

class Animal:
     def sound(self):
        print("Animal makes a sound")
class dog(Animal):
     def sound(self):
        print("dog barks")
class cat(Animal):
     def sound(self):
        print("cat Meow meowwwwww")
d=dog()
b=cat()
b.sound()
d.sound() 

#task_7

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw (self):
        pass
class circle(shape):
    def draw(self):
        print("Drawing a circle")

circle=circle()
circle.draw()        
 
 #task_8

#  class emp:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
#     def get_name(self):
#         return self