from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def area(self):
        return 10*5
r=Rectangle()
print(r.area())        



#task 1 
class Book:
    def __init__(self,Tital,author):
        self.Tital = Tital
        self.author = author

    def intro(self):
            print(f"tital name is {self.Tital} and I am {self.author} this book.")

s1=Book("the fly","jon")
s1.intro()         


#task 2

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def area(self):
        return 10*5
r=Rectangle()
print(r.area())  


class Mobile:
    def __init__(self,battery):
        self.__battery=battery
    def deposit(self,amount):
        self.__battery+=amount

    def get_balance(self):
        return self.__battery
account=(1000)
account.deposit(500)
print(account.get_balance())
                       