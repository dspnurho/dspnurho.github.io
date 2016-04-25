import csv
categories = []
count = 0
with open('New Brother Website Integration-report.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        categories.extend(row)

for item in categories:
    print count
    count = count + 1
    print item, '\n'

categories = categories[1:]

brothers = []
for i in range(17):
    brothers.append(categories[i])

for item in brothers:
    item.append(categories[i+17])

print "lalalala brothers:"
for item in brothers:
    print "\nitem is ", item

