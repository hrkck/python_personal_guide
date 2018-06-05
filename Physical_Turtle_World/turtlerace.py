'''
Created on Mar 20, 2016

@author: bloyd
'''
import turtle
import random

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100, 20)
lance.goto(-100, -20)


# my code

for a in range(10):

    x = random.randrange(1, 50)
    y = random.randrange(1, 50)
    andy.forward(x)
    lance.forward(y)

wn.exitonclick()
