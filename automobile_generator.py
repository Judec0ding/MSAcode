#first automobile is bc of file name, second is automobile class we made inside file
from Automobile import Automobile

def main():
    #create instances of Automobile
    auto1 = Automobile("Honda", "Accord", "23456", 2.2, "Alice", 2017, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")

    #change auto2 year
    auto2.__year = 2000
    #change auto1 owner
    auto1.set_owner("Enzo")
    #change auto2 color
    auto2.set_color("Red")


    auto_list = []
    auto_list.append(auto1)
    auto_list.append(auto2)

    #print each automobile's information
    for auto in auto_list:
        auto.print_data()
    
    print(f"Auto 1 is {auto1.get_age()} years old")


main()