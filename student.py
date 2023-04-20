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

    # This finds the students registration information
    students_courses = [course for course in c_course if id in c_roster[course]]
    
    if student_courses:
        # this counts the number of courses 
        num_courses = len(student_courses)
        
        # shows the courses
        print("courses registered: ")
        for course in student_courses:
            print(f'\t{course}')
        else:
            print(f'Total number: {num_courses}')
    else:
        print("No registered courses found")
    
    print()
    
            

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

    # asks the for the course they want to add
    course = input('enter the course you want to add?')
    course = course.upper()

    # checks if the course is offered
    if course not in c_roster:
        print('Sorry, course is not offered')
        return

    # checks if the student is enrolled in this class already
    if id in c_roster[course]:
        print('Sorry, student is already enrolled in this course')
        return

    # checks if the course is full
    if len(c_roster[course]) >= c_max_size[course]:
        print('Sorry, this course is at max capacity')
        return

    # will add the student to the course
    c_roster[course].append(id)
    print('student has been added to this course')


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
