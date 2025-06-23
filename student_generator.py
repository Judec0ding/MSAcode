# create a student generator that will load student data from the students.csv file
from Student import Student
# open the students.csv file and read it
def main():
    # open file
    data_file = open("students.csv", "r")
    # create a list of students variable to save information later on 
    # and prevent any resetting in loop
    list_of_students = []
    #read each line of data in the data file
    for line in data_file:
        # split the info by the commas
        info = line.split(",")
        # if there aren't 6 items in the list, skip the line by continuing
        if len(info) !=6:
            continue
        try:
            int(info[3])
            float(info[4])
            int(info[5])
        except:
            continue
        
        student = Student(info[0], info[1], info[2], int(info[3]), float(info[4]), int(info[5]))
        list_of_students.append(student)
        student.print_student_data()

    data_file.close()












main()