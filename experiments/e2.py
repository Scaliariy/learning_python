import csv

with open("../files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data:
    if row[0] in city:
        print(row[1])
