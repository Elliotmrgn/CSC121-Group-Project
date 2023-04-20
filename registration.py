# ----------------------------------------------------------------
# Author: Elliot Morgan
# Date: 04/19/2023
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import student
import billing
import bcrypt

def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    # Student ID and PINs for grading (normally this wouldn't be here)
    # ('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')

    student_list = [('1001', b'$2b$12$jTLcwQRKsODvF6OrY5ZI7.IJiI9hJcJJKdY8nV2iaUyWjOgFMpR2G'),
                    ('1002', b'$2b$12$GH9wBGzZ40pGu85NEX3cVeOekeZ7RromAdDISyT0n8YwqcgxWZLDW'),
                    ('1003', b'$2b$12$iR5AIVPGIMt2x5IMQC0alOgrNvSJWP7dkuq.fUDPyNbPrQzdRotFa'),
                    ('1004', b'$2b$12$xbPBik9Ddi6aqOx8r5bk8uSxrN559yMLtc7CowUvqgwiHnnoLhNCy')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    # -----------------------------------------------------------------------

    while True:
        # ID input
        id_input = input("Enter ID to log in, or 0 to quit: ")

        # Break loop on 0 input
        if id_input == "0":
            break

        else:
            # Checks the ID and PIN
            if login(id_input, student_list):

                while True:
                    # Input for user selection
                    user_selection = input(
                        "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")

                    # Break loop on 0 input
                    if user_selection == "0":
                        print("Session ended.\n")
                        break

                    # Add course
                    elif user_selection == "1":
                        student.add_course(id_input, course_roster, course_max_size)

                    # Drop course
                    elif user_selection == "2":
                        student.drop_course(id_input, course_roster)

                    # List courses
                    elif user_selection == "3":
                        student.list_courses(id_input, course_roster)

                    # Show bill
                    elif user_selection == "4":
                        # Since the function returns two arguments, calculate_hours_and_bill is required to have an
                        # asterisk in front of it.
                        billing.display_hours_and_bill(*billing.calculate_hours_and_bill(id_input, student_in_state,
                                                                                         course_roster, course_hours))

                    # Invalid input
                    else:
                        print("invalid input")


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    # PIN input
    pin = str(input("Enter PIN: "))

    # finds the tuple corresponding to the id entered, otherwise returns None
    matched_id = next((s for s in s_list if s[0] == id), None)
    # if student id was found
    if matched_id is not None:
        # checks the input pin to the stored hash
        if bcrypt.checkpw(pin.encode(), matched_id[1]):
            print("ID and PIN verified\n")
            return True
        # Wrong PIN
        else:
            print("ID or PIN incorrect\n")
            return False
    # Wrong ID
    else:
        print("ID or PIN incorrect\n")
        return False


def password_hash(pin):
    # ------------------------------------------------------------
    # This function would be used when creating a new PIN for a student
    # Since we do not have that functionality yet, I manually ran it on each password we were provided
    # It has one parameter: pin, which would be the new PIN entered
    # This function utilizes the bcrypt library to first create a
    # new salt that will be used for hashing. Then combines encoded
    # new PIN and salt to create the hashed_password. It returns
    # this hashed password that can be added to the student_list
    # -------------------------------------------------------------

    salt = bcrypt.gensalt()  # generate a new salt for pin
    # hash the inputted pin (pin must be encoded since it hashes the byte values of the string)
    hashed_password = bcrypt.hashpw(pin.encode(), salt)

    return hashed_password


# Error catch for stopping program prematurely
try:
    main()
except KeyboardInterrupt:
    print(f"\n\nProgram was ended")
