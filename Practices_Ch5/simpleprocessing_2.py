#username.py
# simple string processing proogram to generate usernames

def main():
    print("This program generates computer usenames. \n")
    
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")
    
    uname= first[0] + last[:3]
    print("Your username is:", uname)
    
main()

#if the last name is less than the stated range, then it will output an error