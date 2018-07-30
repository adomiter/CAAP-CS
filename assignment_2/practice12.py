#this program accepts a date in the form month/day/year and outputs whether or not the date is valid

def date_valid(date):
    newdate= date.split("/")
    day= newdate[2]
    month= newdate[1]
    month_day= {"January":31,
               "February":28,
               "March": 31,
               "April": 30,
               "May": 31,
               "June": 30,
               "July": 31,
               "August": 31,
               "September": 30,
               "October": 31,
               "November": 30,
               "December": 31}
    if day > month:
        print("This date is not valid.")
    else: 
        print("This date is valid.")