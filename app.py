# x="hello"
# print(type(x))
# x={1,2,3}
# print(type(x))
# x=["pramav",20]
# print(type(x))
# x={"name":"prnv","age":18}
# print(type(x))
# def f():
#     s="i love steps"
#     print(s)
# f()
def myfunction():
    global x
    x = "fantastic"

# Call the function to set the global variable x
myfunction()

# Print the value of x
# print("python is " + x)


# a=6
# b=8
# c=a+b
# print(a+b)
# d=a-b
# print(d)
# e=a*b
# print(e)
# f=a/b



# a=10
# b=15
# c=100
# print(a+b+c)
# print(a+b)
# d=a-b
# print(d)
# f=c/b
# print(f)
# e=a*b
# print(e)

# a=10
# b=3
# c=a//b
# d=a%b
# print(c)
# print(d)
# a=20
# b=3
# c=a//b
# print(c)
# d=a%b
# print(d)



# a=20
# b=20
# print(a==b)
# print(a!=b)
# a=28
# b=10
# print(a<b)
# print(a>b)
# a=10
# print(a<15 and a>5)
# print(a>2 or a<10)
# a="hello"
# b="world"
# result=a+b 
# print(result)
# print(a*3)
# x="python"
# print(x[1:4])
# x="python"
# print(len(x))
# print(x[5])
# y="spectrum"
# x=y.upper()
# print(x)
# x=y.capitalize()
# print(x)
# y="spectrum"
# x=y.upper()
# print(x)
# a="hello"
# x=a.count("l")
# print(x)
# x="hello,world"
# y=x.index("world")
# print(y)
# y=x.replace("world","universe")
# print(y)
# x="  hello"
# y=x.lstrip()
# print(y)
# x=10
# if x>8:
#     print("x is greater than 8")
# x=20
# if x!=20:
#     print("x is not equal to 20")
# else:
#     print("x is equal to 20")
# x=10
# if x>15:
#     print("x is greater than 15")
# elif x==15:
#     print("x is equal to 15")
# else:
#     print("x is not greater than 15")

# fruits=["apple","banana","orange"]
# for fruit in fruits:
#     print(fruit)
# numbers=[1,2,3,4]
# for mths in numbers:
#     print(mths)
# count=9
# while count <=20:
#     print(count)
#     count +=1
# x=2
# while(x<10):
#     print(x)
# for i in range(10):
#     print(i)
#     if i==2:
#         break
# for x in range(20):
#     print(x)
#     if x==15:``````
#         break
# i=0
# while i<6:
#     print(i)
#     if i==4:
#         break
#     i+=1
# i=0
# while i<5:
#     i+=1
#     if i==2:
#         continue 
#     print(i)
# for x in range(10):
#     x+=1
#     if x==4:
#         continue
#     print(x)
# for x in range (3):
#     for i in range(1,5):
#          print(i,end="    ")
#     print()
# for x in range(6):
#     for i in range(x):
#         print("*",end="") 
#     print()
# x=["apple","banana","cherry"]
# i=list((enumerate(x)))
# print(i)



#####append,insert,remove,pop#####

# a=[1,2,3,"apple"]
# a.append("anu")
# a.insert(1,"orange")
# a.remove("orange")
# a.pop(2)
# print(a) 




####list comprehension###

# x=[x**2 for x in range(1,11)]
# print(x)

# even_squares=[x**2 for x in range(10) if x%2==0]
# print(even_squares)


# tupple_1=(1,2,3,4)
# tupple_2=("apple","mango","orange")
# x=tupple_1+tupple_2
# print(x)



# x={1,2,3,4,5}
# x.add(7)
# print(x)
# y={1,2,3,4}
# a={3,4,5,6}
# b=y|a
# print(b)
# x={1,2,3,4}
# y={4,5,6,7}
# z=x-y
# print(z)
# x={1,2,3,4}
# y={4,5,6,7}
# z=x&y
# print(z)