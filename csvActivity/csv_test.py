import csv

with open('Clustering-Quiz-Record.csv', mode="r", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)