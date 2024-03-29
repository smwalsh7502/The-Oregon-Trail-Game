# Title: The Oregon Trail Game
#   Dev: Samantha Walsh
#  Date: 9/10/2021

# Description:
# This program is a recreation of The Oregon Trail game developed by
# Bill Heinemann, Don Rawitsch, and Paul Dillenberger

# Sources:
# 1  (Oregon Trail Info)https://en.wikipedia.org/wiki/The_Oregon_Trail_(series)
# 2  (Oregon Trail Game)https://classicreload.com/oregon-trail.html
# 3  (If statements)https://www.w3schools.com/python/python_conditions.asp
# 4  (Booleans)https://www.w3schools.com/python/python_booleans.asp
# 5  (Functions)https://www.w3schools.com/python/python_functions.asp
# 6  (Time module)https://www.programiz.com/python-programming/time
# 7  (Operators)https://www.w3schools.com/python/python_operators.asp
# 8  (While loops)https://www.w3schools.com/python/python_while_loops.asp
# 9  (While loops)https://wiki.python.org/moin/WhileLoop
# 10 (Exceptions)https://www.w3schools.com/python/python_ref_exceptions.asp
# 11 (Lists)https://www.w3schools.com/python/python_lists_comprehension.asp
# 12 (Date/Time Module)https://www.w3schools.com/python/python_datetime.asp
# 13 (String Formatting)https://realpython.com/python-string-formatting/
# 14 (Try/Except)https://www.w3schools.com/python/python_try_except.asp
# 15 (.upper)https://www.w3schools.com/python/ref_string_upper.asp
# 16 Andrew Krupp (Student Assistant)
# 17 Prof. Scott Vanselow

# I will refer to these sources by number throughout the program
# I removed all global variables by Prof. Vanselow's recommendation.

###############################################################################

# Importing the time and datetime modules (Source 6)
# Third-Party Libraries have been checked for security issues and are up-to-date
import time
import datetime
from threading import Timer
import random


# Defining functions (Source 5)
def main():
    # INTRODUCTION
    print("Hello! My name is Sam!")
    time.sleep(2)  # Time Module (Source #6)
    print("This is my recreation of the Original Oregon Trail game.")
    print("I hope you enjoy playing! :)")
    time.sleep(2)
    print("-" * 150)  # Using the * String operator
    # Instead of typing "-" 150 times, I told Python to multiply
    # the string "-" by 150.
    time.sleep(2)

    # GAME CHOICES
    print("\nWelcome to the Oregon Trail!")
    time.sleep(2)
    print("""\nMany kinds of people made the trip to Oregon.
    \tYou may:
    \t\t1. Be a banker from Boston
    \t\t2. Be a carpenter from Ohio
    \t\t3. Be a farmer from Illinois
    \t\t4. Find out the differences between these choices\n""")

    # The user will first decide their career
    # The user's career choice will affect their funds, supplies,
    # and ability to survive (later on)

    # I am calling to the functions by assigning the function to a variable.
    # The value returned by the function will be assigned to the variable.
    # These functions will allow the user to decide their career and will
    # determine the amount of money the user will get based on their choice.
    # A function will also allow the user to choose a different career.
    # Then the user will decide the names of the people in their party.
    main_career = career_choice()
    main_funds = career_choice_funds(main_career)
    main_points = career_choice_points(main_career)  # Will use later
    check_career_choice(main_career)
    family_names_list = family_names()  # Will use later
    check_family_names()

    # START GAME
    # The user will decide which month to leave. Later on, this month
    # choice will affect their survival.
    print("""
It is 1848. Your jumping off place for Oregon is Independence, Missouri.
You must decide which month to leave Independence.
    """)
    time.sleep(2)
    print("\t1. March", "2. April", "3. May", "4. June", "5. July",
          "6. Ask for advice\n", sep="\n\t")  # Using sep
    time.sleep(1)
    main_month = month_choice()  # Calling to month_choice() using a variable
    main_day = 1

    # GENERAL STORE INTRO
    print("Before leaving Independence you should buy equipment and "
          "supplies.")
    time.sleep(2)
    print("You have $%.2f in cash but you don't have to spend it all now."
          % main_funds)
    # Formatting strings (Source 13)
    time.sleep(2)
    print("You can buy whatever you need at Lou's general store.")
    time.sleep(2)
    print("\nLet's head there now.\n")
    time.sleep(2)
    print("-" * 150)
    time.sleep(2)

    # LOU'S GENERAL STORE DIALOGUE
    print("\n'Howdy there partner! The names' Louis but you can call me Lou.'")
    time.sleep(2)
    print("'So yer' going to Oregon! Them trails is dangerous...'")
    time.sleep(2)
    print("'Lucky for you, we got everything y'all will need.'")
    time.sleep(2)
    print("'Here's what I recommend for new comers...'")
    time.sleep(2)
    print("(Lou hands you a wrinkled piece of paper.)")
    time.sleep(2)
    print("(The handwriting looks like a child's and it's filled with "
          "spelling mistakes.)")
    time.sleep(2)
    print("(You can just barely make out what it says...)")
    time.sleep(2)
    print("""
\t~ a team of oxen to pull your wagon
\t~ clothing for summer and winter
\t~ plenty of food
\t~ ammunition for your rifles
\t~ spare parts for your wagon\n""")
    time.sleep(3)
    print("-" * 150)
    time.sleep(1)

    # Now I am assigning variables for my general_store() and
    # general_store_calculator() functions.
    main_oxen_spent = 0.00
    main_food_spent = 0.00
    main_clothing_spent = 0.00
    main_ammunition_spent = 0.00
    main_spare_parts_spent = 0.00
    main_amount_spent = 0.00
    main_pay_items = "pay"
    main_exit_store = "exit"

    main_oxen = 1
    main_food = 2
    main_clothing = 3
    main_ammunition = 4
    main_spare_parts = 5

    # Calling to functions with multiple arguments

    general_store_calculator(main_month, main_funds, main_oxen_spent,
                             main_food_spent, main_clothing_spent,
                             main_ammunition_spent,
                             main_spare_parts_spent, main_amount_spent,
                             main_oxen, main_food, main_clothing,
                             main_ammunition, main_spare_parts,
                             main_pay_items, main_exit_store)

    main_inventory = inventory(main_oxen_spent, main_food_spent,
                               main_clothing_spent, main_ammunition_spent,
                               main_spare_parts_spent)

    main_miles = 0
    print("-" * 150)

    trail_day_choices(main_month, main_miles, main_day, main_inventory)


# CAREER CHOICE FUNCTION
# The career choice function allows the user to decide their career.
# This function takes a user input of 1,2,3, or 4. It outputs the user's
# career choice for later use in other functions. If the user picks choice 4,
# the user will receive a description of the choices.

# I had originally had the career_choice() function include the code within
# the career_choice_funds() and career_choice_points() functions however
# Andrew Krupp (Student Assistant) recommended I return only one value
# per function (or do only one thing) instead of three so that it would be
# less confusing.
def career_choice():
    career_info = 4
    user_making_choice = True  # Booleans (Source 4)
    # When user_making_choice is False, the loop will break
    while user_making_choice:  # While loops (Sources 8 and 9)
        try:  # try/except statements (Source 14)
            career = int(input("What is your choice? Type 1,2,3, or 4. "))
            if career == career_info:  # Using == operator (Source 7)
                print("""
\tTraveling to Oregon isn't easy! But if you're a banker, you'll have 
\tmore money for supplies and services than a carpenter or a farmer.

\tHowever, the harder you have to try, the more points you deserve!
\tTherefore, the farmer earns the greatest number of points and the
\tbanker earns the least.\n""")
            # This is the same as saying 0 < career < 6
            elif not career > 0 and not career < 6:  # Using 'and' and 'not'
                print("Sorry, I didn't understand that. Please type 1,2,3, "
                      "or 4. ")
            else:
                user_making_choice = False
                # Break in loop
        except ValueError:  # Built in exception (Source 10)
            print("Sorry, I didn't understand that. Please type 1,2,3, or 4. ")
    return career
    # Return (Source 5)


# CAREER FUNDS
# The career_choice_funds function will take in the parameter of the user's
# career choice from career_choice() and output the amount of money
# they will get based on that choice.
def career_choice_funds(career):
    banker = 1
    carpenter = 2
    farmer = 3
    local_career = career
    if local_career == banker:
        local_funds = 1600.00
    elif local_career == carpenter:
        local_funds = 800.00
    elif local_career == farmer:
        local_funds = 400.00
    return local_funds


# CAREER POINTS
# The career_choice_points function will take in the parameter of the user's
# career choice from career_choice() and output the amount of money
# they will get based on that choice.
def career_choice_points(career):
    banker = 1
    carpenter = 2
    farmer = 3
    local_career = career
    if local_career == banker:
        local_points = 1
    elif local_career == carpenter:
        local_points = 2
    elif local_career == farmer:
        local_points = 3
    return local_points


# For checking if user's input is correct/incorrect in multiple functions
correct = "Y"
incorrect = "N"


# CHECK CAREER CHOICE FUNCTION
# This functions checks if user's career choice was what they wanted and
# allows the user to change their career choice.
def check_career_choice(main_career):
    user_making_choice = True
    while user_making_choice:
        try:
            correct_career = str(
                input("You chose career number " + str(main_career) +
                      ". Is that correct? Type Y or N. "))
            # String Concatenation
            if correct_career.upper() == correct:  # Using .upper() (Source 15)
                print("Great! Next, you will choose the names for the members "
                      "of your party.")
                time.sleep(2)
                print("You will be the wagon leader.")
                time.sleep(2)
                print("You will be traveling your spouse and three kids.")
                time.sleep(2)
                print("-" * 150)
                user_making_choice = False
            elif correct_career.upper() == incorrect:
                print("Which career would you like instead? ")
                career_choice()
            else:
                print("Sorry, I didn't understand that. Please type Y or N.")
        except ValueError:
            print("Sorry, I didn't understand that. Please type Y or N.")


# PRINT FAMILY NAMES FUNCTION
# This function allows the user to input their name and the names of their
# party members. The function then prints out all the family names.
# I use this function in the check_family_names() functions so that if the
# user decides to change a name, it will output the new names.
# This function returns a list containing the string names of the party.
# Later I will user this list to randomize death, injury, and sickness.
def family_names():
    wagon_leader = str(input("What is the name of the wagon leader? "))
    spouse = str(input("What is your spouse's name? "))
    oldest_child = str(input("What is the name of your eldest child? "))
    middle_child = str(input("What is the name of your middle child? "))
    youngest_child = str(input("What is the name of your youngest child? "))
    print("\nOk. Here is your party: ")
    print(" 1. " + wagon_leader)  # String operator +
    print(" 2. " + spouse)
    print(" 3. " + oldest_child)
    print(" 4. " + middle_child)
    print(" 5. " + youngest_child)
    return [wagon_leader, spouse, oldest_child, middle_child, youngest_child]


# CHECK FAMILY NAMES
# The check_family_names() function asks the user whether or not the names
# they entered in the family_names() function is correct.
def check_family_names():
    user_making_choice = True
    while user_making_choice:
        correct_names = str(input("\nAre these names correct? Type Y or N. "))
        if correct_names.upper() == incorrect:
            print("Ok. Please re-enter your party's names\n")
            time.sleep(1)
            family_names()
        elif correct_names.upper() == correct:
            print("\nGreat! We are ready to start.")
            print("-" * 150)
            time.sleep(2)
            user_making_choice = False
        else:
            print("I'm sorry, I didn't understand that. Please type Y or N.")


# Variables used in the month_choice() function
month_name = ["March", "April", "May", "June", "July"]
month_info = 6


# MONTH CHOICE FUNCTION
# This function will ask the user which month of the year they want to leave.
# Their month choice will affect survival of the weather (later on).
# The function returns the month choice which will be used in other
# functions to display the date and later determine the weather.
def month_choice():
    user_making_choice = True
    while user_making_choice:
        try:
            local_month = int(
                input("Which month would you like to leave? Please"
                      " type 1,2,3,4,5, or 6. "))
            if 0 < local_month < 6:
                print("\nOk. You will be leaving for Oregon in " +
                      month_name[local_month - 1] + ".")
                time.sleep(2)
                user_making_choice = False
            elif local_month == month_info:
                print("""
You attend a public meeting held for "folks with the California-Oregon fever."
You're told:
\t"If you leave too early, there won't be any grass for your oxen to eat.
\tIf you leave too late, you may not get to Oregon before winter comes.
\tIf you leave at just the right time, there will be green grass
\tand the weather will still be cool."\n""")
            else:
                print("Sorry, I didn't understand that. "
                      "Please type 1,2,3,4,5, or 6. ")
        except ValueError:  # Built in exception ---> Source # 11
            print("Sorry, I didn't understand that. "
                  "Please type 1,2,3,4,5, or 6. ")
    return local_month


# GENERAL STORE
# This function will display the date, their item options, how much they've
# spent (Will start at 00.00), and how much money they have. This function
# is used in the general_store_calculator function so that after each
# item is selected and purchased, the general_store() function will display
# the new amount.
def general_store(local_month, local_funds, local_oxen, local_food,
                  local_clothing, local_ammunition, local_spare_parts,
                  local_amount):
    date = datetime.datetime(1848, local_month + 2, 1)
    print("-" * 150)
    print("\nLou's General Store \nIndependence, Missouri")
    print(date.strftime("%B %d, %Y\n"))  # Date/Time ---> Source #13
    print("Items Available:         Amount spent per item:")
    print(" 1. Oxen                 $" + format(local_oxen, '.2f'))
    print(" 2. Food                 $" + format(local_food, '.2f'))
    print(" 3. Clothing             $" + format(local_clothing, '.2f'))
    print(" 4. Ammunition           $" + format(local_ammunition, '.2f'))
    print(" 5. Spare Parts          $" + format(local_spare_parts, '.2f')
          )
    print("-" * 50)
    print("Amount you have:         $" + format(local_funds, '.2f'))
    print("Total cost:              $" + format(local_amount, '.2f'))
    print('\nType "Pay" to Pay for Items')  # Pay for items
    print('Type "Exit" to exit the store\n')  # Leave Store
    print("-" * 150)


# GENERAL STORE CALCULATOR
# This function will ask the user how many items they want and calculate the
# amount the user owes. The function will also tell the user if they don't have
# enough money and will kick them out of the store if they don't have enough.
# I have to use many parameters for this function because I am using variables
# from the main() function. It works great :)
def general_store_calculator(local_month, local_funds, local_oxen, local_food,
                             local_clothing, local_ammunition,
                             local_spare_parts, local_amount,
                             oxen, food, clothing, ammunition,
                             spare_parts, pay_items, exit_store):
    user_making_choice = True
    while user_making_choice:
        general_store(local_month, local_funds, local_oxen, local_food,
                      local_clothing, local_ammunition, local_spare_parts,
                      local_amount)
        item_choice = input("Which item would you like to purchase? Please "
                            "type 1,2,3,4, or 5. ")
        if str(item_choice) in pay_items:
            # If the user has enough money, they will pay.
            if (local_funds - local_amount) >= 0.00:
                print("Your total is $" +
                      str(local_oxen + local_food + local_clothing +
                          local_ammunition + local_spare_parts))
                time.sleep(2)
                print("You now have $" + str(local_funds - local_amount) +
                      " left.")
                time.sleep(2)
                local_funds -= local_amount
            # If the user does not have enough money, they will be kicked out.
            elif (local_funds - local_amount) < 0.00:
                print("'What in tarnation?! You haven't got a penny "
                      "to your name. Get out of my store 'for I "
                      "call the police.'")
                time.sleep(2)
                print("You have exited the store.")
                user_making_choice = False
                time.sleep(1)
        elif str(item_choice) in exit_store:
            # If the user does not want to purchase anything they can exit.
            print("You have exited the store.")
            user_making_choice = False
            time.sleep(2)
        elif int(item_choice) == oxen:
            # If the user picked oxen (1) they will be asked how many they want
            print("\n\t'There are 2 oxen in a yoke. "
                  "I recommend at least 3 yoke.'")
            print("\t'I charge $40 a yoke.'\n")
            number_of_items = float(input("\t'How many yoke do you want?' "
                                          ""))
            print("\t" + str(number_of_items) + " yoke is " +
                  str(number_of_items * 2) + " oxen.")
            time.sleep(2)
            print("\tThat will cost: $" + (str(number_of_items * 40.00)))
            time.sleep(2)
            # Calculating the cost based on the number of items the user wants
            local_oxen += (number_of_items * 40.00)
            local_amount += (number_of_items * 40.00)
            time.sleep(1)
        elif int(item_choice) == food:
            # If the user picked food (2) they can pick how much they want.
            print("""\n\t'I recommend you take at least 200 pounds of 
\tfood for each person in your family. I see that you have 
\t5 people in all. You'll need flour, sugar, bacon, and coffee. 
\tMy price is 20 cents a pound.'\n""")
            number_of_items = float(input("\t'How many pounds of food "
                                          "do you want? "))
            print("\t" + str(number_of_items) + " pounds of food will give "
                                                "each person " + str(
                number_of_items / 5) + " pounds of "
                                       "food to eat.")
            time.sleep(2)
            # Then it will calculate the cost and how many pounds of food
            # each person will get.
            print("\tThat will cost: $" + (str(number_of_items * 0.20)))
            local_food += (number_of_items * 0.20)
            local_amount += (number_of_items * 0.20)
            time.sleep(1)
        elif int(item_choice) == clothing:
            # If the user picked clothing (3)
            print("""\n\t'You'll need warm clothing in the mountains. 
\tI recommend taking at least 2 sets of clothing per person. 
\tEach set is $10.'\n""")
            number_of_items = float(input("\t'How many sets of clothes "
                                          "do you want? "))
            print("\tOk. You will have " + (str(number_of_items // 5)) +
                  " sets of clothing per person.")
            time.sleep(2)
            # It will display how many sets of clothing each family
            # member will have.
            if (number_of_items % 2) == 0:
                print("\tEach person will have the same number of "
                      "clothing sets.")
            elif (number_of_items % 2) != 0:
                print("\tUh oh! Someone will not have the same number of "
                      "clothes as everyone else.")
            time.sleep(2)
            # Using the modulus % operator to determine if each family member
            # has the same number of clothes.
            print("\tThat will cost: $" + (str(number_of_items * 10)))
            local_clothing += (number_of_items * 10)
            local_amount += (number_of_items * 10)
            time.sleep(1)
        elif int(item_choice) == ammunition:
            # If the user picked ammunition (4)
            print("\n\t'I sell ammunition in boxes of 20 bullets. "
                  "Each box costs $2'")
            number_of_items = float(input("\t'How many boxes of bullets "
                                          "do you want?' "))
            print("\tOk. That will cost: $" + str(number_of_items * 2))
            local_ammunition += (number_of_items * 2)
            local_amount += (number_of_items * 2)
            time.sleep(1)
        elif int(item_choice) == spare_parts:
            # If the user picked spare parts (5)
            print("""\n\t'It's a good idea to have a few spare parts 
\tfor your wagon. Spare parts cost $10 each.'""")
            number_of_items = float(input("\t'How many spare parts do you"
                                          " want?' "))
            print("\tOk. That will cost: $" + str(number_of_items * 10))
            local_spare_parts += (number_of_items * 10)
            local_amount += (number_of_items * 10)
            time.sleep(1)
        elif int(item_choice) < 1 or int(item_choice) > 5:
            print("Sorry, I didn't understand that. Please "
                  "type 1,2,3,4,5, Pay, or Exit.")
            # If the user did not type 1,2,3,4,5 pay, or exit.
            time.sleep(1)


# INVENTORY
# The inventory() function uses the amount spent in the
# general_store_calculator() function to keep track of the amount of items in
# in the user's inventory. This is calculated based off the cost
# of each of the items. I used floor division so that it is rounded to
# a whole number.
def inventory(local_oxen_spent, local_food_spent, local_clothing_spent,
              local_ammunition_spent, local_spare_parts_spent):
    num_oxen = (local_oxen_spent // 40.00) * 2  # Floor Division
    num_food = local_food_spent // 0.20
    num_clothing = local_clothing_spent // 10.0
    num_ammunition = local_ammunition_spent // 2.0
    num_spare_parts = local_spare_parts_spent // 10.0
    return [num_oxen, num_food, num_clothing, num_ammunition, num_spare_parts]


# HUNTING
# The hunting() function gives the user a time limit to type BANG
# If the user types BANG correctly within the time limit, they
# will get a random amount of food between 50 and 200 pounds. The user
# only gets three tries at hunting total. Every time a shot is fired
# 5 boxes of bullets are used. This is because one "day" in the oregon trail
# is actually worth two weeks.

# This still needs work on the timing.
def hunting(local_inventory):
    food = 1
    ammunition = 3
    for tries in range(3):
        timeout = 2
        t = Timer(timeout, print, ["Sorry, you weren't quick enough!"])
        t.start()
        hunt_bang = input("QUICK! Type BANG: ")
        t.cancel()
        if hunt_bang == "BANG":
            print("\nRight between the eyes! You got a big one!")
            local_meat = random.randint(50, 200)
            print("You got " + str(local_meat) + " pounds of meat!")
            local_inventory[ammunition] -= 5
            local_inventory[food] += local_meat
            time.sleep(1)
        else:
            print("Better luck next time!")
            choice = input("Would you like to try again? Type y or n. ")
            if choice.upper() == correct:
                continue
            elif choice.upper() == incorrect:
                break
    print("\nI think that's enough hunting for today.")


# RATIONS
# The rations function allows the user to determine how they will ration
# their food for the next two weeks. Poor is 1 pound of food per person, per
# day. Moderate is 2 pounds of food per person, per day. Well is 3 pounds of
# food per person, per day.
def rations(local_inventory):
    food = 1
    family = 5
    user_making_choice = True
    while user_making_choice:
        try:
            local_rations = int(input("What is your choice? "))
            if local_rations == 1:
                print("You and your family will eat poorly for the next two "
                      "weeks. This may impact your health. ")
                if local_inventory[food] - ((1 * family) * 14) < 0:
                    print("I'm sorry, you do not have enough food for that. "
                          "You need to go hunting.")
                    hunting(local_inventory)
                elif local_inventory[food] - ((1 * family) * 14) >= 0:
                    local_inventory[food] -= ((1 * family) * 14)
                    user_making_choice = False
            elif local_rations == 2:
                print("You and your family will eat moderately for the next "
                      "two weeks. Your family is ok with this.")
                if local_inventory[food] - ((2 * family) * 14) < 0:
                    print("I'm sorry, you do not have enough food for that. ")
                elif local_inventory[food] - ((2 * family) * 14) >= 0:
                    local_inventory[food] -= ((2 * family) * 14)
                    user_making_choice = False
            elif local_rations == 3:
                print("You and your family will eat moderately for the next"
                      "two weeks. You're family seems happy about this.")
                if local_inventory[food] - ((3 * family) * 14) < 0:
                    print("I'm sorry, you do not have enough food for that. ")
                elif local_inventory[food] - ((3 * family) * 14) >= 0:
                    local_inventory[food] -= ((3 * family) * 14)
                    user_making_choice = False
            else:
                print("I'm sorry, I didn't understand that. Please type 1,"
                      "2, or 3.")
        except ValueError:
            print("I'm sorry, I didn't understand that. Please type 1,"
                  "2, or 3.")


# TRAIL CHOICES
# The trail day choices function will be the repeating day function that
# allows the user to make choices along the trail. It will print the
# date, the miles travelled, and the amount of items in their inventory.
# It will also allow the user to decide if the want to hunt and how to
# ration their food for the next two weeks. Later, I will create a function
# that determines the weather, their health, and randomizes events.
# This function in main() will loop 12 turns. If the user survives 12 turns
# they will win the game.
def trail_day_choices(local_month, local_miles, local_day, local_inventory):
    date = datetime.datetime(1848, local_month + 2, local_day)
    local_oxen = "Oxen:"
    local_food = "Food:"
    local_clothing = "Clothing:"
    local_ammunition = "Ammunition:"
    local_spare_parts = "Spare parts:"
    print(date.strftime("%B %d, %Y\n"))
    print("-" * 50)
    print("Total miles travelled: " + str(local_miles))
    print("%-15s %-15s %-15s %-15s %s" % (local_oxen, local_food,
                                          local_clothing, local_ammunition,
                                          local_spare_parts))
    for item in range(len(local_inventory)):
        print("%-15s" % str(local_inventory[item]), end="")
    print("\n-" * 50)
    user_making_choice = True
    while user_making_choice:  # user decides if they want to hunt
        try:
            local_hunt = int(input("Do you want to hunt (1) or "
                                   "continue (2)? "))
            if local_hunt == 1:
                hunting(local_inventory)  # Call to the hunting() function
                user_making_choice = False
            elif local_hunt == 2:
                print("Ok. Let's continue.")
                user_making_choice = False
            else:
                print("I'm sorry, I didn't understand that. "
                      "Please type 1 or 2. ")
        except ValueError:
            print("I'm sorry, I didn't understand that. Please type 1 or 2. ")
    print("How do you want to ration your food?")
    print("""Do you want to eat: 
\t1. Poorly
\t2. Moderately
\t3. Well""")
    rations(local_inventory)  # Call to the rations() function


# Call to main()
main()
