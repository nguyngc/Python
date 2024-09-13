# 7. Tuple, set, and dictionary

# 1. Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.
def season_of_the_month(month_number):
    season = ("Spring", "Summer", "Autumn", "Winter")
    return season[int(month_number/3) -1]

month_input = int(input("Enter the number of a month: "))
if month_input <= 12:
    print(f"The corresponding season is {season_of_the_month(month_input)}")
else:
    print("Invalid value!!!")


# 2. Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.
names = set()
while True:
    name = input("Please enter a name: ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("List name:")
for n in names:
    print(n)


# 3. Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code
# and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and
# prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times
# they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of
# Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)
airports = {}
while True:
    print("Which action do you want to do?")
    print("1. Enter a new airport")
    print("2. Fetch the information of an existing airport")
    print("3. Quit")
    action_input = int(input("Choose: "))

    if action_input == 1:
        print("Please input the information of the new airport")
        airport_icao_code = input("ICAO code: ")
        airport_name = input("Name:")
        airports[airport_icao_code] = airport_name
    elif action_input == 2:
        airport_icao_code = input("Please input the ICAO code: ")
        if airport_icao_code in airports:
            print(f"The airport name is: {airports[airport_icao_code]}")
        else:
            print("There is no information for this airport.")
    elif action_input == 3:
        break
    else:
        print("Invalid action!!!")


