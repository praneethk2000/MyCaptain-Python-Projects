# Basic school administration tool

import csv

# Function to create a csv file to add the entries
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)

# Used to write the header for the data
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-mail ID"])

# Used to write the contents of the data
        writer.writerow(info_list)
if __name__ == '__main__':
# Added condition for the loop to check in order to add more srtudent information
    condition = True
    # Initialise the student number. Will increment as more data is entered.
    student_num = 1

    # Loop taken to add multiple student information
    while(condition):
        student_info = input("Please enter student information for student number {} in the folllowing Format:Name Age Contact Number E-mail ID: ".format(student_num))

# Made into a list to be compatible for storing as a csv format.
        student_info_list = student_info.split(" ")

        print("Entered information is - \n Name: {}\n Age: {}\n Contact Number: {}\n E-mail Id: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

# Choice check to verify if entered student information is correct
        choice_check = input("Is the entered information correct? (Yes/No): ")

        if choice_check == 'Yes':
            write_into_csv(student_info_list)

# Condition check to ask user if they want to add more information
            condition_check = input("Enter Yes/No if you want to enter more student information: ")
            if condition_check == "Yes":
                condition = True
                student_num +=1
            elif condition_check == 'No':
                condition = False
        elif choice_check == 'No':
            print("Please re-enter the entries")
