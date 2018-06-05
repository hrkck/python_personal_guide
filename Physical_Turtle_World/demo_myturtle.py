'''
Created on May 21, 2016

@author: hrkucuk
'''

# DEMO FILE OF PHYSICAL TURTLE WORLD
# BELOW, NEWTONS'S LAW OF MOTION IN ONE DIMENSION IS CODED.
# RESPECT.

import turtle
import myturtle

# Window Settings
wn = turtle.Screen
wn.bgcolor("lightblue")
wn.screensize(1920 * 2, 1080 * 2)

# Initializing the Turtle
agirabi = myturtle.myTurtle(1)  # Turtle's mass is 1
agirabi.speed(3)
print(agirabi.mass)
# Positioning the Turtle:
agirabi.up()
agirabi.goto(-300, 0)
agirabi.down()

# Initial Force is applied:
agirabi.setForce(300)
# for lack usability of the screen, the turtle must turn around manually.
# Just omit this one:
a = 1

# Steps of for loop somehow represents the "time":
for i in range(30):

    # Just omit these part:
    #####################
    if a == 8:
        agirabi.left(90)
        agirabi.forward(20)
        agirabi.left(90)
    if a == 24:
        agirabi.right(90)
        agirabi.forward(20)
        agirabi.right(90)
    agirabi.dot(3)
    a += 1
    #####################

    # It moves with its velocity:
    agirabi.forward(agirabi.getVel())
    agirabi.write("%d : %d : %d " %
                  agirabi.getInfoForce() + ": %d" % agirabi.getVel())

    # Then, the force is reseted to zero.
    # We will see that the Turtle will keep moving with its initial velocity,
    # Until friction stops it.
    agirabi.setForce(0)
    # END OF LOOP


wn.exitonclick()
