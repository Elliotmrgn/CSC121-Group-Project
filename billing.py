# ----------------------------------------------------------------
# Author: Chase Smith
# Date: 4/3/2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters:
    #
    # id, the student id;
    # s_in_state, the list of in-state students;
    # c_rosters, the rosters of students in each course;
    # c_hours, the number of hours in each course.
    #
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------

    # Assign isInState to a boolean:
    is_in_state = s_in_state[id]

    # Adjust credit hour costs if the student is located in the state:
    cost_per_credit_hour = 850
    total_tuition_cost = 0
    total_credit_hours = 0
    if is_in_state:
        cost_per_credit_hour = 225

    # Loop through the course roster dictionary:
    for course, students in c_rosters.items():

        # If the student's id is found in the course roster...
        if id in students:
            # Add the credit hours to the total
            total_credit_hours += c_hours[course]

            # Set the total tuition cost with augmented addition operator
            # to the (cost of a credit hour * credit hours of the course)
            total_tuition_cost += (cost_per_credit_hour * c_hours[course])

    # Return the calculated results:
    return total_credit_hours, total_tuition_cost


def display_hours_and_bill(hours, cost):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------

    # Straight forward output function
    print(f'Course load: {hours} credit hours')
    print(f'Enrollment cost: ${cost:.2f}\n')
