from turtle import *
import random

def tree(branchLen, turt):
    if branchLen > 5:
        turt.forward(branchLen)
        turt.right(45)
        tree(branchLen-random.randint(5,15), turt)

        turt.left(90)
        tree(branchLen-random.randint(5,15), turt)

        turt.right(45)
        turt.backward(branchLen)

t = Turtle()
wind = Screen()
t.speed(9)
t.up()
t.left(90)
t.backward(100)
t.down()
t.color("green")
tree(75, t)

wind.exitonclick()
