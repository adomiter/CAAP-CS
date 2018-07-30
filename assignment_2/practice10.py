#modify the above program 
def Easter(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19a + 24)%30
    e = (2b+4c+6d+5)%7
    exceptions = {"1954",
                 "1981",
                 "2049",
                 "2079"}
    if year == exceptions;
        print("The date for Easter in", year,"is April", (22+d+e)-24, "," year)
    elif (22+d+e) > 31:
        print("The date for Easter in", year,"is April", (22+d+e)-31, "," year)
        
def main():
    year =int(input("What is the year?"))
    Easter(year)
main()
        
    