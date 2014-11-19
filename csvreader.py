import csv

with open(r'C:\Python27\ENES100.CSV','rb') as csvfile:
    contents = csv.reader(csvfile)
    for students in contents:
        want = students[0:2]
        print ' '.join(want)



