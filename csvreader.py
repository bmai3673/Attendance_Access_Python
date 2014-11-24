import csv

with open(r'C:\Python27\ENES100.CSV','rb') as csvfile:
    contents = csv.reader(csvfile)
    var = raw_input("what do you need?\n" +
                "1 Student Name\n" +
                "2 ID Number\n" +
                "3 Section\n" +
                "4 Grade 1\n" +
                "5 Grade 2\n" +
                "6 Grade 3\n")
    print (var)

    for students in contents:
        value = ""

        if "1" in var:
            value = value + students[0] + "; "

        if "2" in var:
            value = value + students[1] + "; "

        if "3" in var:
            value = value + students[2] + "; "

        if "4" in var:
            value = value + students[3] + "; "

        if "5" in var:
            value = value + students[4] + "; "

        if "6" in var:
            value = value + students[5] + "; "
            
        print value
