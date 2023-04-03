# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import student
import billing


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

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
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
        id_input = input("Enter ID, 0 to quit: ")

        # Break loop on 0 input
        if id_input == "0":
            break

        else:
            # Checks the ID and PIN
            if login(id_input, student_list):
                print("ID and PIN verified\n")

                while True:
                    # Input for user selection
                    user_selection = input(
                        "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit:")

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

            # Wrong ID and/or PIN
            else:
                print("ID or PIN incorrect\n")


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    # PIN input
    pin_input = input("Enter PIN: ")

    # combines ID and PIN into a tuple and checks if it exists in the student list
    if (id, pin_input) in s_list:
        return True
    else:
        return False


main()
