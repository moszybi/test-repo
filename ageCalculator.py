from datetime import datetime

monthsInAYear = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
daysOtheWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
present_year = datetime.now().strftime("%Y")


def getYr():
    presentYr_int = int(present_year)
    lowest_limit = 1900

    x = input("Enter your year of birth in digits\n").strip()
    try:
        x = int(x)
    except:
        print("Error, invalid year of birth. Enter year in numbers!!!")
        x = getYr()
    else:
        if x < lowest_limit: # Alternatively this can be used, 1900 > x > present_year.
            print(f"Error, Year of birth must not be less than {lowest_limit}.")
            x = getYr()
        if x >= presentYr_int:
            print(f"Error, Year of birth must not be greater than {present_year}.")
            x = getYr()

    return x


def getMth():
    monthVal = input("Enter your month of birth in digits\n").strip()
    try:
        #if the try block returns true, the else block will execute.
        #if the try block returns false, the except block will execute.
        #followed by the finally block.
        """sequence of execution is 1st and 3rd block OR 2nd and 4th (last) block."""
        yResultMonth = int(monthVal)
    except:
        print("String value detected.")
    else:
        if yResultMonth <= 11:
            monthIndex = yResultMonth
        if yResultMonth > 11:
            print("Input Error, value entered 'Larger' than expected.")
            monthIndex = getMth()
        if yResultMonth < 1:
            print("Input Error, value entered 'Smaller' than expected.")
            monthIndex = getMth()
    finally:
        for month in monthsInAYear:
            if monthVal in month:
                monthIndex = monthsInAYear.index(month)
                monthIndex += 1

    print("\n")
    return monthIndex


def dayObirth():
    dayVal = input("Enter your date of birth in digits\n").strip()
    try:
        #if the try block returns true, the else block will execute.
        #if the try block returns false, the except block will execute.
        #followed by the finally block.
        """sequence of execution is 1st and 3rd block OR 2nd and 4th (last) block."""
        zResultDay = int(dayVal)
    except:
        print("String value detected.")
    else:
        if zResultDay <= 31:
            dayIndex = zResultDay
        if zResultDay > 31:
            print("Input Error, value entered 'Larger' than expected.")
            dayIndex = dayObirth()
        if zResultDay < 1:
            print("Input Error, value entered 'Smaller' than expected.")
            dayIndex = dayObirth()
    finally:
        for day in daysOtheWeek:
            if dayVal in day:
                dayIndex = daysOtheWeek.index(day)

    print("\n")           
    return dayIndex

#Defaul Values of Month of birth, Day of birth and Year of birth.
my_MOB = "Default"
my_DayOB = "Default"
my_YOB = "Default"

def ageCalculator(yOB,mOb,dayOfb):
    global my_MOB, my_YOB, my_DayOB

    my_DateOB = datetime(yOB,mOb,dayOfb)
    my_DayOB = my_DateOB.strftime("%A")
    my_MOB = my_DateOB.strftime("%B")
    my_YOB = my_DateOB.strftime("%Y")

    myCurrentAge = int(present_year) - int(my_YOB)
    print("\n")
    return myCurrentAge


yOB = getYr()#Gets the year input from user
monthOfB = getMth() #Gets the month input from user.
dayOfb = dayObirth()#Gets the day in digits or day in words inputed by user

myAge = ageCalculator(yOB,monthOfB,dayOfb)
print(f"You were born in {my_YOB}. You will be {myAge} yrs old this {my_MOB.capitalize()}, {present_year}!!!")