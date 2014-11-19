""" The purpose of this program is to take an excel spreadsheet that was converted
into a CSV fileand then create a python program that will read the file and the program
will allow you to choose which list you want to access. Basically, if you
only wanted to see the student name and ID#, then you could tell the program
to display only that data and not everything else. The output of this program
needs to display the data without the commas"""

import csv
dictionary = {
    "names":["Smith, John", "Jane, Mary", "Peter, Parker", "Spiderman"],
    "identification":[2345789, 4872985, 483749, 3457688],
    "classes":["ENES100-2014FA-501", "ENES100-2014FA-501", "ENES100-2014FA-501", "ENES100-2014FA-501", "ENES100-2014FA-501"],
    "grade_1":[12, 60, 88],
    "grade_2":[55, 70, 90],
    "grade_3":[99, 20, 1]
}
print "what type of information do you need?: students, ID, course, grade_1, grade_2, grade_3"
settle = raw_input()
if settle == "students":
    print dictionary['names']
elif settle == "ID":
    print dictionary['identification']
elif settle == "course":
    print dictionary['classes']
elif settle == "grade_1":
    print dictionary['grade_1']
elif settle == "grade_2":
    print dictionary['grade_2']
elif settle == "grade_3":
    print dictionary[csv.'grade_3']
else:
    print "wut"
