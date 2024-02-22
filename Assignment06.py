# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   NVC, 2024/02/19, Created Script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import json

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
MENU: str = '''
~~~~~~ Course Registration Program ~~~~~~
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
FILE_NAME: str = "Enrollments.json"

students: list = []  # a table of student data
menu_choice: str  # Holds the choice made by the user.

# ~~~~~~~~~~~~~~~~~~~~~~ Processing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    NVC, 2024.02.19, Created Class
    NVC, 2024.02.19, Added a function to read file
    NVC, 2024.02.19, Added a function to write to the file
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
       This function reads data from the json file

       ChangeLog: (Who, When, What)
       NVC, 2024.02.19,Created Class

       :return: student_data

       """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            print(student_data)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This functions writes information to the already existing Json file

        ChangeLog: (Who, When, What)
        NVC, 2024.02.19,Created Class

        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The data has been saved to the file!")
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Presentation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    NVC, 2024.02.19,Created Class
    NVC, 2024.02.19, Added menu output and input functions
    NVC, 2024.02.19, Added a function to display the data
    NVC, 2024.02.19, Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        NVC, 2024.02.19,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        NVC, 2024.02.19, Created function

        :return: None
        """
        print()
        print(MENU)  # separate function
        print()

    @staticmethod
    def input_menu_choice():
        """This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        NVC, 2024.02.19, Created function

        :return: string with the user's menu choice
        """

        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the information necessary to register for a course:
            student's first name, last name and course to enroll in

        :return: None
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)

            # students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data. Try again!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student's names and course they're registered for

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        RRoot,1.4.2030,Added code to toggle technical message off if no exception object is passed

        :return: None
        """
        print("~" * 50)
        print("Current enrollment information: ")
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("~" * 50)


# End of function definitions

# Beginning of the main body of the script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:

    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
