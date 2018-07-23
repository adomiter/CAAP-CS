import math

def circleArea(radius):
    area=float((math.pi)*(radius**2))
    return area

def cost_perinch(circleArea, price):
    cost=(float(price)/float(circleArea))
    print("The cost per square inch is", cost,"dollars.")
    
def main():
    diameter=float(input("What is the diameter of the pizza?"))
    radius=diameter/2
    dollar=float(input("What is the price of the pizza?"))
    
    squareinch=(circleArea(radius))
    cost_perinch(squareinch, dollar)

main()
    