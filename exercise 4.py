# 4. While loops (while)
import math
import random


# 1. Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
i = 1
print("Below are the list number divisible by three in the range of 1-1000")
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i = i + 1


# 2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
while True:
    input_number = int(input("Please enter a number (inches): "))
    if input_number < 0:
        break
    print(f"{input_number} inches =", input_number * 2.54, "centimeters.")


# 3. Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
input_number = input("Please enter a number: ")
if input_number != "":
    smallest_number = largest_number = int(input_number)
    while True:
        input_number = input("Please enter a number: ")
        if input_number == "":
            break
        input_number = int(input_number)
        if smallest_number > input_number:
            smallest_number = input_number
        if largest_number < input_number:
            largest_number = input_number

    print(f"The smallest number is {smallest_number}, and the largest number is {largest_number}.")


# 4. Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
random_number = int(random.randint(1, 10))
guess_number = 0
while guess_number != random_number:
    guess_number = int(input("What is your number? "))
    if guess_number < random_number:
        print("It is too low.")
    elif guess_number > random_number:
        print("It is too high.")
print("Correct!")


# 5. Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.
user_name = 'python'
password = 'rules'
retry_times = 0
print("Please input:")
while retry_times < 5:
    name = input("Username: ")
    pwd = input("Password: ")
    if name == user_name and pwd == password:
        print("Welcome.")
        break
    retry_times = retry_times + 1
if retry_times == 5:
    print("Access denied.")


# Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around
# the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle
# A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number of random points,
# such as one million, inside square B. Let N be the total number of random points. Each point inside the square is tested
# for whether it resides inside circle A. Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
random_points = int(input("How many random points to be generated? "))
inside_points = 0
i = 0
while i < random_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_points += 1
    i += 1

pi = 4 * inside_points / random_points
print(f"The approximation value of pi is: {pi}.")
print(f"The difference with math pi is: {math.pi - pi}.")
