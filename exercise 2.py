import math
import random

# 1. Write a program that asks your name and then greets you by your name
name = input("What is your name? ")
print("Hello", name, "!")

# 2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = float(input("What is the radius of the circle? "))
print("Area of the circle is", radius**2 * math.pi)

# 3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
rectangle_length = float(input("What is the length of the rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
print("The perimeter of the rectangle is", 2*(rectangle_length + rectangle_width))
print("The area of the rectangle is", rectangle_length * rectangle_width)

# 4. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers
print("Please give three integer numbers:")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
total = num1 + num2 + num3
print("Sum =", total)
print("Product =", num1 * num2 * num3)
print("Average =", total/3)

# 5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.
print("Enter talents:")
talents = float(input())
print("Enter pounds:")
pounds = float(input())
print("Enter lots:")
lots = float(input())
total = (((talents * 20) + pounds) * 32 + lots) * 13.3
print(f"The weight in modern units: {int(total // 1000)} kilograms and {total % 1000: .2f} grams.")

# 6. Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.
print(f"A 3-digit code where each number is between 0 and 9 is: {random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
print(f"A 4-digit code where each number is between 1 and 6 is: {random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}")
