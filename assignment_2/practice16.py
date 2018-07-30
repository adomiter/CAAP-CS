#was not able to download graphics.py

from graphics import *
def target():
    win = GraphWin()
    aCircle= Circle(Point(0,0), 100)
    aCircle.setFill("white")
    aCircle2= Circle(Point(0,0), 80)
    aCircle2.setFill("black")
    aCircle3= Circle(Point(0,0), 60)
    aCircle3.setFill("blue")
    aCircle4= Circle(Point(0,0), 40)
    aCircle4.setFill("red")
    aCircle5= Circle(Point(0,0), 20)
    aCircle5.setFill("yellow")
        
def main():
    target()
    score=0
    for i in range(5):
        p=win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
        if p.getX() <20 and p.getY() <20:
            score= 9
        elif p.getX() <40 and p.getY() <40:
            score= 7
        elif p.getX() <60 and p.getY() <60:
            score = 5
        elif p.getX() <80 and p.getY() <80:
            score =3
        else:
            score =1
        score += score 
main()
            
        
            
    
        