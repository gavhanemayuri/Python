#calling function
def greet():
    print("hello welcome to python!")
greet()                                              #def ext down


#function with parameters
def greet(name):
    print("hello",name)
    #calling the function
greet("mayuri")  


#function with multiple paramenters
def add(a,d):
    print(a+d)
          #calling
add(5,3)


#function with return value
def add(a,d):
    return a*d
                           
result=add(4,25)
print(result)


#function without arguments but with return
def square():
    return 5*5

print(square())


#real life ex
def claculate_parcentage(total,obtained):
    percentage = (obtained/total)*100
    return percentage

print(claculate_parcentage(500,425))