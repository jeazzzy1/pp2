# 1 
import math
x = int(input("Input degree:"))
print("Output radian:", math.radians(x))

#2
height=int(input("height:"))
x = int(input("Base, first value:"))
y = int(input("Base, second value:"))
print(float(x+y))

#3
n = int(input("Input number of sides:"))
l = int(input("Input length of side:"))
cot = 1/math.tanh(180/n)
print("The area of the polygon is:", (n * l**2 * cot)/4)
 
 #4
lofb=int(input("Length of base:"))
h = int(input("Height of parallelogram:"))
print("Expected Output:", float(lofb * h))