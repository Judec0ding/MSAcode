# create a student generator that will load student data from the students.csv file
from datetime import datetime
from Student import Student
# open the students.csv file and read it
"""
Function to write an error message to a log file
Input: (str)error message
Output: None
"""
def write_to_error_log(message:str) -> None:
    # open the log file in append mode: error_log.txt
    the_date = datetime.now()
    error_log = open("error_log.txt", "a")
    #or; with open("error_log.txt", "a") as error_log:

    # write error message to the file in the format 
    # date: message -> 6/24/2025: Error in data file on line 5
    error_log.write(f"{the_date}: {message}")
    # close file
    error_log.close()
    #return to main funtion, RETURN NOT NECESSARY
    return


"""
Function to return a list of student objects
Input: none
Output: list of student objects
"""
def load_students() ->list[Student]:
    # open file
    data_file = open("students.csv", "r")

    # create a list of students variable to save information later on 
    # and prevent any resetting in loop
    list_of_students = []
    # or list_of_students: list[Student] = []
    # create a line_number to store the line value
    line_number = 0
   
    # read each line of data in the data file
    for line in data_file:
        # add 1 to line number
        line_number += 1
        # split the info by the commas
        info = line.split(",")
        # if there aren't 6 items in the list, skip the line by continuing
        if len(info) !=6:
            # write an error message to an error log 
            write_to_error_log(f"Format error in data file on line {line_number}\n")
            # and continue down the file
            continue
        try:
            # make sure info is correct by making sure they're numbers
            int(info[3])
            float(info[4])
            (info[5])
        except:
            # if not, write an error message to the error log
            # and continue down the file
            write_to_error_log(f"Format error in data file on line {line_number}\n")
            continue
        
        # student is equal to the the parts of information in the line of the file, that align with Student class objects
        student = Student(info[0], info[1], info[2], int(info[3]), float(info[4]), (info[5]))
        # add the student to the list_of_students
        list_of_students.append(student)
        # print the data for each student in list_of_students
    data_file.close()
    return list_of_students
    # DONT forget to close the file

"""
Function to convert student objects to student dictionaries
Input: list of student objects
Output: list of student dictionaries
"""
def student_to_dictionary(list_of_students:list[Student]) -> list[dict]:
    # create a list to store the dictionaries in
    student_dictionary_list = []
    # loop through the student list and write each student's data to a dictionary 
    for student in list_of_students:
        # create an empty dictionary
        student_dictionary = {}
        # set the keys and values for the dictionary 
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id_number()
        
        # append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    
    # return the list of dictionaries
    return student_dictionary_list

"""
Function to get a list of student dictionaries
Input: none
Output: list of student dictionaries
"""
def get_student_dictionaries():
    # get a list of students 
    student_list = load_students()

    # get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)
    
    return student_dictionaries
