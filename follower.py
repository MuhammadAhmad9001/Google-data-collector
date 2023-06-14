######################### OOP with python #####################
"""
class Dog:
    attr1 = "animal"
    attr2 = "dog"
    
    def fun(self):
        print("i am ",self.attr1)
        print("i am ",self.attr2)
        
Roger = Dog()

print(Roger.attr1)
Roger.fun()

"""


################################


"""
class Person:
    def __init__(self,name):
        self.name = name
        
    def say_hi(self):
        print('hello, my name is ',  self.name)
        
p = Person('Nikhil')
p.say_hi()

"""

###########################3333

"""
class Dog:
    
    animal = 'dog'
    
    def __init__(self,breed,color):
        
        self.breed = breed
        self.color = color
        
Rodger = Dog("pug" , "brown")
Buzo = Dog("bulldog" , "black")

print('Rodger details')
print('Rodger is a ', Rodger.animal)
print('breed ',Rodger.breed)
print('color',Rodger.color)

print('\nBuzo details')
print('Buzo is a ', Buzo.animal)
print('breed ',Buzo.breed)
print('color',Buzo.color)

print("\naccessing class variable using class name")
print(Dog.animal)

"""

#############################

"""
class camaal:
    
    anaimal = 'camaal'
    
    def __init__(self,breed):
        self.breed = breed
        
    def setcolor(self,color):
        self.color = color
    
    def getcolor(self):
        return self.color
    
maraunt = camaal("cool")
maraunt.setcolor("black")
print(maraunt.getcolor())
        





class add:
    first = 0
    second = 0
    answer = 0
    
    def __init__(self,f,s):
        self.first = f
        self.second = s
    
    def display(self):
        print("first number =" + str(self.first))
        print("second number =" + str(self.second))
        print("addition numbers =" + str(self.answer))
        
    def calculation(self):
        self.answer = self.first + self.second
        
obj = add(1000,2000)

obj.calculation()

obj.display()
        
"""


class Emmployee:
    
    def __init__(self):
        print('hello to work')
        
    def __del__(self):
        print('emplyee bye del')
    
obj = Emmployee()
del obj
    