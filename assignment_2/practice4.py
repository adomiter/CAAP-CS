#write a program that calculates class standing from the number of credits earned
def class_standing(credits):
    if credits < 7:
        print("Freshman")
    elif credits >= 7 and credits <16:
        print("Sophomore")
    elif credits >= 16 and credits <26:
        print("Junior")
    else:
        print("Senior")
    
def main():
    credits = int(input("What is the number of credits earned?"))
    class_standings(credits)
main()