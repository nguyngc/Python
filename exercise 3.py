# 3. Conditional structures (if)


# 1. Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size
# limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters
# below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

zander_limit = 42
zander_length = int(input("What is the size of the zander? "))
if zander_length < zander_limit:
    miss_length = zander_limit - zander_length
    print("Your caught fish was", miss_length, "centimeters below the size limit.")
    print("It does not fulfill the size limit, please release the fish back into the lake!")
    print("A zander must be 42 centimeters or longer to meet the size limit.")
else:
    print("Yay! Your caught fish meet the size limit.")


# 2. Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written
# description according to the list below. You must use an if/elif/else structure in your solution.
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

cabin_class = input("What is your cabin class of a cruise ship? ")
if cabin_class == "LUX":
    print("It is an upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("It is a cabin above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("It is a windowless cabin above the car deck.")
elif cabin_class == "C":
    print("It is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


# 3. Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("What is your gender (F/M)? ")
hemoglobin = int(input("What is your hemoglobin value? "))
if gender == "F":
    if hemoglobin < 117:
        print("Your hemoglobin is too low.")
    elif hemoglobin > 155:
        print("Your hemoglobin is too high.")
    else:
        print("Your hemoglobin is normal.")
elif gender == "M":
    if hemoglobin < 134:
        print("Your hemoglobin is too low.")
    elif hemoglobin > 167:
        print("Your hemoglobin is too high.")
    else:
        print("Your hemoglobin is normal.")
else:
    print("Invalid value!!!")


# Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.

input_year = int(input("Please enter a year: "))
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(input_year, "is a leap year.")
else:
    print(input_year, "is not a leap year.")