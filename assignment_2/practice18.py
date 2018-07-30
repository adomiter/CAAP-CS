#this is excercise 3 from chapter 6

def sphereArea(radius):
    area= 4*(math.pi)*(radius**2)
    print("The area of the sphere is",area,".")
    
def sphereVolume(radius):
    volume= (4/3)*(math.pi)*(radius**3)
    print("The volume of the sphere is",volume,".")

def main():
    rad=int(input("What is the radius of the sphere?"))
    if rad > 0:
        sphereArea(rad)
        sphereVolume(rad)
    else:
        print("This is not a valid radius.")
main()