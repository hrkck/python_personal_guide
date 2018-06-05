class RectanglePrism(object):

    height = 0
    width = 0
    length = 0

    def __init__(self, h, w, l):
        self.height = h
        self.width = w
        self.length = l

    def calculateVolume(self):
        return self.height * self.width * self.length

    def calculateArea(self):
        return (self.height * self.width + self.height + self.length + self.width * self.length) * 2


class Sphere(object):

    radius = 0

    def __init__(self, r):
        self.radius = r

    def calculateVolume(self):
        return (4 / 3) * (self.radius**3) * (3.14)

    def calculateArea(self):
        return (4) * (self.radius**2) * (3.14)
