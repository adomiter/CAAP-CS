#outputs the total sum of numbers entered by the user 
def sum_numbers (): 
    totalnumbers=eval(input("How many numbers do you want to input?"))
    thesum= 0
    
    for i in range(totalnumbers):
        number=eval(input("What number do you want to add?"))
        thesum= number + thesum
    
    print("The sum of the numbers above is: ", thesum)
    
sum_numbers()