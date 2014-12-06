import csv

""" For this code to work for whatever CSV file is being used, some of the
information below will need to be altered because this code works for the
small sample CSV file that comes along with it. """

with open(r'C:\Python27\ENES100.CSV','rb') as csvfile:
    contents = csv.reader(csvfile)
    
    var = raw_input("what do you need? All numbers require a semi-colon after the number.\n" +
                "1 Student Name\n" +
                "2 ID Number\n" +
                "3 Section\n" +
                "4 Grade 1\n" +
                "5 Grade 2\n" +
                "6 Grade 3\n" +
                "10 Test value\n" +
                "14 Second Test Number\n")
    print (var)

    for students in contents:
        value = ""

        if "1;" in var:
            value = value + students[0] + "; "

        if "2;" in var:
            value = value + students[1] + "; "

        if "3;" in var:
            value = value + students[2] + "; "

        if "4;" in var:
            value = value + students[3] + "; "

        if "5;" in var:
            value = value + students[4] + "; "

        if "6;" in var:
            value = value + students[5] + "; "
        
        if "10;" in var:
            value = "Test for number 10"

        if "14;" in var:
            value = "Test for number 14"

        print value

       """ Numbers 10 and 14 do not work properly when entered in with
any of the single digit numbers. This is most likely because it is not
pulling from the CSV file """
