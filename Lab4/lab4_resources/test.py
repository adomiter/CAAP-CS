#tests the draw function using one image

import turtle
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")

boxSize = 10

myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0) 

def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)     

pallet_8 = ["#F0F0F0", "#8A360F", "#000000"]
pixels_8 = [[0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_8.append([0,0,0,2,2,1,1,1,1,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0])
pixels_8.append([0,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0])
pixels_8.append([0,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,0,0,0,0,0,0,0,0,2,1,2,0,0,0])
pixels_8.append([2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,0,0,0,0,0,0,0,2,1,2,0,0,0])
pixels_8.append([2,1,0,1,1,1,1,1,1,1,1,2,2,1,1,1,1,2,0,0,0,0,0,0,0,2,1,2,0,0])
pixels_8.append([2,1,2,1,1,1,1,0,2,1,1,2,2,1,1,1,1,2,0,0,0,0,0,0,0,2,1,2,0,0])
pixels_8.append([2,1,2,1,1,1,1,2,2,1,1,2,2,1,1,1,1,2,0,0,0,0,0,0,0,2,1,2,0,0])
pixels_8.append([0,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,2,0,0,0,0,0,0,2,1,1,2,0,0])
pixels_8.append([0,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,0,0,0,2,2,2,2,2,2,1,2,0,0])
pixels_8.append([2,0,2,2,1,1,1,1,1,1,1,2,1,1,1,2,0,0,2,2,1,1,1,1,1,1,2,0,0,0])
pixels_8.append([2,2,2,2,1,1,1,1,1,2,2,2,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,0,0])
pixels_8.append([2,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0])
pixels_8.append([0,2,2,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0])
pixels_8.append([0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0])
pixels_8.append([0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0])
pixels_8.append([0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2])
pixels_8.append([0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
pixels_8.append([0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,2])
pixels_8.append([0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,0,0,2,1,1,2])
pixels_8.append([0,0,0,0,0,0,0,2,1,2,1,1,2,1,1,1,1,2,2,2,1,1,2,0,0,0,2,1,1,2])
pixels_8.append([0,0,0,0,0,0,2,1,1,2,2,2,2,1,1,1,2,0,0,2,2,2,2,0,0,2,1,1,1,2])
pixels_8.append([0,0,0,0,0,0,2,1,1,2,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,2,2,2,2,0])
pixels_8.append([0,0,0,0,0,2,1,1,1,2,0,0,2,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,2,2,2,2,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def draw_test():
    for i in pixels_8:
        for j in i:
            myPen.color(pallet_8[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def main():
    print("This is a list of drawing pieces you can choose from:")
    print("1. Banana")
    print("2. Mario")
    print("3. PacMan Ghost")
    print("4. Purple Monster")
    print("5. Mushroom")
    print("6. Smiley Face")
    print("7. Panda")
    print("8. Dog")
    num= int(input("Which one would you like to draw?"))
    if num == 1:
        draw(pallet_1, pixels_1)
    elif num == 2:
        draw(pallet_2, pixels_2)
    elif num == 3:
        draw(pallet_3, pixels_3)
    elif num == 4:
        draw(pallet_4, pixels_4)
    elif num == 5:
        draw(pallet_5, pixels_5)
    elif num == 6:
        draw(pallet_6, pixels_6)
    elif num == 7:
        draw(pallet_7, pixels_7)
    elif num == 8:
        draw_test()
    else:
        print("This was not one of the choices")
    
    turtle.done()

main()
  