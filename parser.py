import csv
import sys
if len(sys.argv) != 2:
    print("usage: python parser.py [applications.csv]")
    print("output: applications.txt")
    sys.exit()

try:
    f = open('applications.txt', 'w+')
    #fi = open('pre-registration.csv')
    fi = open(sys.argv[1])
    reader = csv.reader(fi)
    data = list(reader)
    for i in data:
        f.write("---------------NEW PROSPECT----------------")
        counter = 0
        f.write("\n")
        f.write("\n")
        for j in i:
            if counter == 0:
                counter = counter + 1
                continue
            if counter == 1:
                f.write("First Name: \b")
            elif counter == 2:
                f.write("Last Name: \b")
            elif counter == 3:
                f.write("Email: \b")
            elif counter == 4:
                f.write("Year: \b")
            elif counter == 5:
                f.write("Major: \b")
            counter = counter + 1
            f.write(j)
            print(j)
            f.write("\n")
            f.write("\n")
        f.write("---------------END PROSPECT----------------\n")
    print("File write completed")
except IOError:
    print("Cannot open")
