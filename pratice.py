# name = input('Please type in a name: ')
# dob = input('Please type in a year: ')
# print(f"{name} is a valiant knight, born in the year {dob}. One morning {name} woke up to an awful racket: a dragon was approaching the village. Only {name} could save the village's residents")
from unicodedata import numeric, decimal

# number_day = input('How many days: ')
# print("seconds =", int(number_day) * 24 * 60 * 60)

eat_times = input("How many times a week do you eat at the student cafeterial? ")
lunch_price = input("The price of a typical student lunch? ")
groceries = input("How much money do you spend on groceries in a week? ")
total = int(eat_times) * float(lunch_price) + float(groceries)
print("Average food expenditure:")
print("Daily:", total/7, "euros")
print("Weekly:", total, "euros")
