#converts temperatures from Fahrenheit to Celsius
def temp_converter (): 
    fahrenheit=eval(input("What is the temperature in Fahrenheit?"))
    x=-32.0+fahrenheit
    celsius=(5.0/9.0)*x
    for i in range(5):
        print("The temperature is", celsius,"celsius.")
temp_converter()

 