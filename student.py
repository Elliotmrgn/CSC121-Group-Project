# ----------------------------------------------------------------
# Author:
# Date:
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------
    pass  # temporarily avoid empty function definition


def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    
    # This asks the user to enter the course that they want to add
    course = input("Enter the course you want to add: ")
    course = course.upper()

    # This checks if the course is offered
    if course not in c_roster:
        print("Error: Course not offered.")
        return

    # This checks if the student has already registered for this course
    if id in c_roster[course]:
        print("Error: Student already registered for this course.")
        return

    # This checks if the course is full
    if len(c_roster[course]) >= c_max_size[course]:
        print("Error: Course is full.")
        return

    # This then adds the student ID to the courses roster
    c_roster[course].append(id)
    print("Student successfully added to the course.")



def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------
    pass  # temporarily avoid empty function definition
