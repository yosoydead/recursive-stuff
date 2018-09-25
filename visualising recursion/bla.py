from turtle import *

t = Turtle()
wind = Screen()

#i use penup so that when the turtle is repositioned, it doesn't draw any lines
t.penup()

#starting position
t.setposition(-300,-300)

#make the turtle draw again
t.pendown()

#this is for speed test
t.speed(9)

#the method needs a turtle object to use to draw things
#lineLen is just the length of the first line
def draw(turtle, lineLen):
    #if the lineLen reaches 0, the program will stop
    if lineLen> 0:
        #just move the turtle from left to right a certain distance
        turtle.forward(lineLen)
        #after drawing the first line, turn a certain angle at the left,
        turtle.left(90)
        #recall function
        draw(turtle, lineLen-5)


draw(t, 500)
wind.exitonclick()