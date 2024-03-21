#1
import math
degrees = float(input("Degree: "))
radians = degrees * (math.pi / 180)
print(round(radians,6))

#2
h = float(input("Height: "))
b1 = float(input("Base1: "))
b2 = float(input("Base2: "))
trapezoid = 0.5 * (b1 + b2) * h
print(trapezoid)

#3
import math

num_sides = 4
side_length = 25

polygon = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
print("Number of sides:", num_sides)
print("Length of a side:", side_length)
print("Polygon area:", polygon)

#ex4
l = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
parallelogram = l*h
print(parallelogram)