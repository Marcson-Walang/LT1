#Marcson Dojan A. Walang  8 - Sampaguita LT1

import math

radius = float(input("Enter the radius of the radius of the garden in meters: "))

area = math.pi * (radius ** 2)

circumference = 2 * math.pi * (radius ** 2)

sqrt_area = math.sqrt(area)

area_roundeddw = math.floor(area)
area_roundedup = math.ceil(area)

print(f"Area of the Garden: {area:.2f} square meters")
print(f"Circumference of the Garden: {circumference:.2f} meters")
print(f"Square root of the Garden: {sqrt_area:.2f}")
print(f"Area rounded down: {area_roundeddw:.2f} square meters")
print(f"Area rounded up: {area_roundedup:.2f} square meters")


