#converts weight from kilograms to pounds
def weight_converter (): 
    print("This program will convert weight from kilograms to pounds.")
    kilogram=eval(input("What is the weight in kilograms?"))
    pounds=2.204623*kilogram
    print("The weight is", pounds,"pounds.")
weight_converter()