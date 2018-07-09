#prints hello to screen
def hello_world (): 
    print("Hello!")
    name=input("What is your name?")
    color=input("What is your favorite color?")
    ice_cream=input("What is your favorite ice-cream flavor?")
    #print("Your name is",name,"and your favorite color is",color,". Also, your favorite ice-cream flavor is",ice_cream,".")
    print("Your name is %s and your favorite color is %s. Also, your favorite ice-cream flavor is %s." % (name,color,ice_cream))
hello_world ()