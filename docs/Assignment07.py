#-----------------------------#
# Title: Assignment07
# Description: Script that stores data in a binary file
# Change Log: (Who, When, What)
# Lauren Parker, 11.29.20, Created script
#-----------------------------#
import pickle # Imports the Pickle Module

# ---------------------------------------- Data ---------------------------------------- #
str_name = ""
int_birth_year = int
lst_data = []
objFile = None

# ---------------------------------------- Processing ---------------------------------------- #

def save_data_to_file(file_name, list_of_data):
    obj_file = open(file_name, "ab")
    pickle.dump(list_of_data,obj_file)
    obj_file.close()

def read_data_fm_file(file_name):
    obj_file = open(file_name, "rb")
    lst_of_data = pickle.load(obj_file)
    obj_file.close()
    return lst_of_data

# ---------------------------------------- Presentation (I/O) ---------------------------------------- #

# Gets user's name and birth year
str_name = str(input("Please enter your name: "))
try:
    int_birth_year = int(input("Please enter the year you were born: "))
except ValueError: # Provides error message in case user does not input integer
    print("Error: Please enter a number for your birth year!")
    int_birth_year = int(input("Please enter the year you were born: "))
except:
    print("Something went wrong")
lst_data = [str_name,int_birth_year]
print(lst_data)
print("*****************")
print() # Adds blank line for presentation

# Asks user if they would like to save their data to a binary file
y_n_input = str(input("Would you like to save your input to a file? Please choose 'y' or 'n': ")).lower()
if y_n_input == 'y':
    save_data_to_file("BirthYear.dat", lst_data)
    print("Your data has been saved!")
    print() # Adds a blank row for presentation
    input("Press Enter to continue:")
elif y_n_input == 'n':
    print("Your file has not been saved.")
    print()  # Adds a blank row for presentation
    input("Press Enter to continue:")

# Asks user if they would like to read their data from binary file
y_n_input = str(input("Would you like to load your data from the file? Please choose 'y' or 'n': ")).lower()
if y_n_input == 'y':
    print("Here is your data:")
    print(read_data_fm_file("BirthYear.dat"))
    input("Press Enter to exit:")
elif y_n_input == 'n':
    print("No worries, thanks anyways!")
    print()  # Adds a blank row for presentation
    input("Press Enter to exit:")