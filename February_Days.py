# February_Days.py Grant Andrews 2/18/22 This program takes a year as user input and tells the user if the year is a leap year or not,
# along with the number of days in February of that year.


# print the purpose of the program to the screen
print("This program tests if a year is a leap year or not.")         


# while loop that will indefinitely run until a user inputs a valid year
# if user does not enter a valid year then print a prompt to user to enter a valid year
while True:                                                                      
    try:
        year = int(input("What year do you want to test?\n"))
        break
    except ValueError:
        print("Please enter a valid year.")
    
    
# determine if the year is a leap year or not. 
# if the year is divisible by 100 and by 400, it is a leap year
# if the year is not divisible by 100, but it divisible by 4, it is a leap year
# in all other instances the year is not a leap year
# print the determination of the leap year along with the number of days in February of that year to the user
if year % 100 == 0:
    if year % 400 == 0:
        print("The year", year, "is a leap year. \nThere are 29 days in February this year.")
    else:
        print("The year", year, "is not a leap year. \nThere are 28 days in February this year.")
else:
    if year % 4 ==0:
        print("The year", year, "is a leap year. \nThere are 29 days in February this year.")
    else:
        print("The year", year, "is not a leap year. \nThere are 28 days in February this year.")