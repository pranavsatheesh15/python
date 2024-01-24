# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter (self):
#         pass
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14* self.radius
# class square(shape):
#     def __init__(self,side_length):
#         shape.side_length=side_length
#     def area(self):
#         return self.side_length**2
#     def perimeter(self):
#         return 4* self.side_length
# circle=circle(radius=5)
# square=square(side_length=4)
# print("circle  -  area:",circle.perimeter())
# print("square  -area:",circle.perimeter()) 


# # static methord

# class MathOperators:
#     @staticmethod
#     def add(x,y):
#         return x+y
#     @staticmethod
#     def substract(x,y):
#         return x-y
# result_add= MathOperators.add(3,6)
# result_substract=MathOperators.substract(6,9)
# print("Result of additition:",result_add)
# print("Result of substraction:",result_substract)


# class variable

class counter:
    count=0
    def __init__(self):
        counter.count +=1
isinstance1=counter()
isinstance2=counter()
isinstance3=counter()
print("number of instance created:",counter.count)
  


class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(f"{dog1.name} is a {dog1.species}.")
print(f"{dog2.name} is also a {dog2.species}.")
print(f"All dogs are {Dog.species}.")

