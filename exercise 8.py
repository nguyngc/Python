# 8. Using relational databases
import mysql.connector
import geopy.distance

db_connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ngoc',
    autocommit=True
)

# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name
# and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.
def get_airport_by_icao(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport of CIAO code {icao} has name {row[0]} and location {row[1]}")
    else:
        print(f"There is no airport with ICAO code {icao}.")
    return

icao_code = input("Please enter the ICAO code of an airport: ")
get_airport_by_icao(icao_code)


# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
def get_airport_by_area_code(area_code):
    sql = f"SELECT name, type FROM airport WHERE iso_country = '{area_code}' ORDER BY type"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(result)
    else:
        print(f"There is no airport in the area code {area_code}.")
    return

area_code = input("Please enter the area code: ")
get_airport_by_area_code(area_code)


# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.
def get_airport_coordinates_by_icao_code(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao_code}'"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

icao_code_1 = input("Please input the ICAO code for airport 1: ")
coordinate_1 = get_airport_coordinates_by_icao_code(icao_code_1)
icao_code_2 = input("Please input the ICAO code for airport 2: ")
coordinate_2 = get_airport_coordinates_by_icao_code(icao_code_2)
print(f"The distance between 2 airport is {geopy.distance.distance(coordinate_1, coordinate_2).km:.0f}km")