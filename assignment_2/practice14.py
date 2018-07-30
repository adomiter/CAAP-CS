##was not able to download graphics.py library

from graphics import *

def line_int(radius, y_intercept):
    if radius**2-y_intercept**2 > 0:
        aCircle = Circle(Point(0,0), radius)
        aLine=Line(Point(-50,y_intercept), Point(50, y_intercept))
        x=(math.sqrt(radius**2-y_intercept**2))
        win.plot(x, y_intercept, "red")
        win.plot(-x, y_intercept, "red")
        aPoint1= Point(x, y_intercept)
        aPoint2= Point(-x, y_intercept)
        print(aPoint1.getX())
        print(aPoint2.getX())
    else:
        print("These are not acceptable inputs. x is undefined.")
    
def main():
    x = int(input("What radius do you want?"))
    y= int(input("What y-intercept do you want?"))
    line_int(x, y)
main()
    
    
    