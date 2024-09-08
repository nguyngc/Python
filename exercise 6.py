# 6. Functions
import math
import random

# 1. Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
def dice_roll1():
    return random.randint(1, 6)
i = 1
while True:
    num = dice_roll1()
    print(f"Dice roll {i} is {num}")
    if num == 6:
        break
    i += 1

# 2. Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function
# you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in
# the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.
def dice_roll2(side):
    return random.randint(1, side)

dice_sides = int(input("How many sides does your dice have? "))
i = 1
while True:
    num = dice_roll2(dice_sides)
    print(f"Dice roll {i} is {num}")
    if num == dice_sides:
        break
    i += 1


# 3. Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def convert_gas(gallons):
    return gallons * 3.7854

while True:
    input_gas = int(input("Please input the volume in gallons: "))
    if input_gas < 0:
        break
    print(f"The value in liters is: {convert_gas(input_gas)}")


# 4. Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.
def sum_of_list(list_int):
    total = 0
    for i in list_int:
        total += i
    return total

def print_list(message, input_list):
    print(message, end=": ")
    for i in input_list:
        print(i, end=" ")

def random_list():
    ex_list = []
    for i in range(10):
        ex_list.append(random.randint(1, 10))
    return ex_list

list1 = random_list()
print_list("The list of number is", list1)
print(f"\nSum of all the numbers in the list = {sum_of_list(list1)}")


# 5. Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
# the same as the original list except that all uneven numbers have been removed. For testing, write a main program
# where you create a list, call the function, and then print out both the original as well as the cut-down list.
def even_number_list(list_int):
    new_list = []
    for i in list_int:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

list2 = random_list()
new_list = even_number_list(list2)
print_list("Original input list", list2)
print_list("\nCut-down list", new_list)


# 6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter
# the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
def unit_price(diameter, price):
    pizza_area = (diameter / 200. ) ** 2 * math.pi
    return price / pizza_area

pizza_diameter_1 = int(input("\nWhat is the diameter of pizza 1? "))
pizza_price_1 = float(input("What is the price of the pizza 1? "))
unit_price_1 = unit_price(pizza_diameter_1, pizza_price_1)

pizza_diameter_2 = int(input("What is the diameter of pizza 2? "))
pizza_price_2 = float(input("What is the price of the pizza 2? "))
unit_price_2 = unit_price(pizza_diameter_2, pizza_price_2)

if unit_price_1 < unit_price_2:
    print("Pizza 1 provides better value for money.")
else:
    print("Pizza 2 provides better value for money.")