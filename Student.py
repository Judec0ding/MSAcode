class Student():

    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number.strip()


    #set and get methods for the class to either set a new value or obtain a value    
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
    
    def get_first_name(self):
        return self.__first_name
    
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_last_name(self):
        return self.__last_name
    
    def set_major(self, new_major):
        self.__major = new_major
    
    def get_major(self):
        return self.__major
    
    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
    
    def get_gpa(self):
        return self.__gpa
    
    def get_id_number(self):
        return self.__id_number
    
    #determines the class based on credit hours and returns the class
    def get_class_level(self):
        if self.__credit_hours <=30:
            return "Freshman"
        elif self.__credit_hours <=60:
            return "Sophomore"
        elif self.__credit_hours <=90:
            return "Junior"
        else:
            return "Senior"
    
    def update_credit_hours(self, additional_credit_hours):
        self.__credit_hours += additional_credit_hours

    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}\nClass Level: {self.__credit_hours}, Major: {self.__major}\nGPA: {self.__gpa}, ID: {self.__id_number}\n")
    


