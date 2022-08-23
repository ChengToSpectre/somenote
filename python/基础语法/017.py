#  #define f .... == f = lambda ....

x = lambda a:a+10
print(x(7))

x = lambda a,b,c : a+b+c
print(x(4,5,6))

cars=[]
cars.append("dasdad")
cars[0]="cars"
l = len(cars)
print(l)
print(cars[0])
print("*"*30)

def func(n):
    a = 100

    def inner_func1():
        s = a+n
        return s

    def inner_func2():
        s = a*n
        return s

    return inner_func2()

f = func(10) 
print(f)

print('-'*30)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("Bill", 63)
# p1.myfunc()

class car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def output(self):
        print(self.name)

c1 = car("car1", 100)
c1.output() 