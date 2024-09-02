# 5. List structures and iterative loops (for)
import random

# 1. Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
dice = int(input("How many dice you want to roll? "))
total = 0
for n in range(dice):
    num = random.randint(1, 6)
    print(f"Dice {n} => {num}")
    total += num
print(f"Total = {total}")


# 2. Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
input_numbers = []
while True:
    input_number = input("Please enter a number: ")
    if input_number == "":
        break
    input_numbers.append(int(input_number))
input_numbers.sort(reverse=True)
print(f"Five greatest numbers: {input_numbers[0:5]}")


# 3. Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
input_number = int(input("Please input an integer: "))
prime_number = 0
for i in range(2, input_number - 1):
    if input_number % i == 0:
        prime_number = 1
        break
if prime_number == 0:
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")


# 4. Write a program that asks the user to enter the names of five cities one by one (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.
city_names = []
for i in range(5):
    city_name = input("Enter the name of city: ")
    city_names.append(city_name)

for n in city_names:
    print(f"{n}")

