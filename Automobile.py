import datetime

class Automobile():

    #define a constructor
    #the constructor defines what happens when we create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year, color):
        #define class properties with values with the parameter values
        #make class properties directly inacessible using underscores
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year
        self.__color = color

    #create getter and setter methods  
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, new_size:int):
        self.__engine_size = new_size

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner:str):
        self.__owner = new_owner

    def get_year(self):
        return self.__year
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color:str):
        self.__color = new_color


    #create a method to print Automobile data
    def print_data(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}, Engine Size: {self.__engine_size}")
        print(f"Owner: {self.__owner}, Color: {self.__color}\n")

    
    #create a method to get the automobile's age
    def get_age(self):
        #get the current year
        the_date = datetime.datetime.now()
        this_year = the_date.year

        #return the difference between the current year and the auto year as the age
        return this_year - self.__year
    