import sys
import random

#testing python version
print(sys.version)

#simple printing
print ("hello World")

#testing variables
height = 1.8
intro = "My name is Charls"
x = 3
y = 4
z = x + y

print(height)
print(type(height))

print(intro)
print(x)
print(type(x))

a = str(3)
b = int(1.0)
c = float(1)

print(a)
print(type(a))
print(b)
print(c)

color = ["red", "green" ,"blue"] #this is a list
l, m, n = color # this is called unpacking

print(l , ", " , m , ", " , n)

print('Hello','World')

#python numbers
print(random.randrange(1,20))

#python strings
multi_Intro = """My name is Charls
and I am a 21 year old CpE Student
who want to learn and master Python
as his primary language credential"""

print(multi_Intro)

name = "CHARLS"

for j in name:
    print(j)




