import turtle
from Point import Point
from Marble import *


def click(a,b):
    print(a,b)

def marble_ex():
    return Marble(Point((-100),(100)), "red") , Marble(Point((-50),(100)), "blue")

def marble_identifier(x,y, c = marble_ex()):
    marble_1 = c[0]
    marble_2 = c[1]
    if marble_1.clicked_in_region(x,y):
        print("you clicked marble 1 - red")
        marble_1.draw_empty()
    elif marble_2.clicked_in_region(x,y):
        print("you clicked marble 2 - blue")
    else:
        print("you did not click marble 1 or two")

def main():
    marble_1 = Marble(Point((-100),(100)), "red")
    marble_2 = Marble(Point((-50),(100)), "blue")
    marble_3 = Marble(Point((0),(100)), "green")
    marble_4 = Marble(Point((50),(100)), "brown")

    win = turtle.Screen()
    win.title("Student Turtle")
    win.setup(700,700)

    list_name = [marble_1, marble_2, marble_3, marble_4]
    for i in range(len(list_name)):
        list_name[i].draw()

    turtle.listen()
# onscreen click method will take a function
#that has at least 2 parameters
#it will pass x,y to the two parameters
    win.onscreenclick(marble_identifier)


if __name__ == "__main__":
    main()
