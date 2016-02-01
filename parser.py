import csv
fi = open('example.csv')
reader = csv.reader(fi)
data = list(reader)
for i in data:
    print(i)
