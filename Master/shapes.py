class Shape:

    def __init__(self, solid):
        self.solid = solid

class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):


