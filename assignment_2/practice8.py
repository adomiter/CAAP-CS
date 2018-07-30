#this program accepts a person's age and years of citizenship as input and outputs and their eligibility for the Senate and House
def eligibility(person_age, citizenship)
    if person_age >= 30 and citizenship >= 9:
        print("This person is eligible for the Senate and House")
    elif person_age >= 25 and citizenship >= 7:
        print("This person is eligible for the House")
    else: 
        print("This person is not eligible for neither the Senate or the House")

def main():
    person_age= int(input("Age:"))
    citizenship= int(input("Years of Citizenship:"))
    eligibility(person_age, citizenship)
main()