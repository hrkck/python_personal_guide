'''
Created on May 22, 2016

@author: hrkucuk
'''
# CLASS FILE OF THE INHERITED TURTLE OBJECT
# BELOW, PHYSICAL WORLD RESPECT TO NEWTON'S LAW OF MOTION IS CODED.
# RESPECT.

import turtle

# Real world settings:
gravity = 10
time = 1  # Not neccessarily created. But it makes the concept easy to follow.
k = 1  # Friction constant


class myTurtle(turtle.Turtle):  # Parent class "turtle.Turtle" is inherited.

    # All these variables below could be, and actually should be, coded as
    # seperate objects. But in this case it just works fine:
    force, frictionForce, netForce, mass, acc, vel = 0, 0, 0, 0, 0, 0

    # Constructor. It only takes "mass" parameter. I think it makes sense.
    def __init__(self, m):
        # Constructor from super class is inherited.
        super(myTurtle, self).__init__()
        # From now on, everything is easy to follow if NEWTON'S LAWS OF MOTION
        # is understood by the audience:
        self.mass = m
        self.frictionForce = k * self.mass * gravity

    # These huge method sets all the ACCELERATION and VELOCITY variables when a force is applied.
    # Our physical world works a little bit complicated, but in a manner of sense. I tried to code all these logic.
    # According to the direction of the force, different situations occur. The first three main "if statements" are about "direction of force" problem.
    # When no force is applied, the friction force must anyway interact with the current velocity, UNLESS VELOCITY IS NOT ZERO.
    # #################################################################################################################################################
    # Q1. There MAY BE still problems in FIRST and SECOND "if statements". I.E. what if the force is negative (-) and the velocity is negative (-), too?
    # A1. Experiment it and figure out.
    # Q2. Of course, something as important as VELOCITY should not be declared completly dependent on a method about FORCE.
    # A2. Creating seperate objects for these variables and using threads in
    # python must solve the issue.
    def setForce(self, f):
        self.force = f
        if (self.force < 0):
            self.netForce = (abs(self.force) - self.frictionForce) * (-1)
            self.acc = self.netForce / self.mass
            self.vel += self.acc * time
        if (self.force > 0):
            self.netForce = (abs(self.force) - self.frictionForce) * (1)
            self.acc = self.netForce / self.mass
            self.vel += self.acc * time
        if (self.force == 0):
            self.netForce = 0
            if(self.vel < 0):
                self.acc = (self.frictionForce / self.mass)
                self.vel = self.vel + self.acc * time
                if self.vel > 0:
                    self.vel = 0
            if(self.vel > 0):
                self.acc = (self.frictionForce / self.mass) * (-1)
                self.vel = self.vel + self.acc * time
                if self.vel < 0:
                    self.vel = 0
            else:
                pass

    # Other easy crap below:
    def getVel(self):
        return self.vel

    def getInfoForce(self):
        return (self.force, self.frictionForce, self.netForce)

    def getForce(self):
        return self.force

    def getFrictionForce(self):
        return self.frictionForce

    def getNetForce(self):
        return self.netForce

    def getMass(self):
        return self.mass

# Force


class Force():

    fTurtle = turtle.Turtle

    def __init__(self, turt):
        self.fTurtle = turt

# Friction Force


class FrictorForce():

    fTurtle = turtle.Turtle

    def __init__(self, turt):
        self.fTurtle = turt
