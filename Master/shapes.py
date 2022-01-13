class Shape:

    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def draw(self):
        print("\u25CF" if self.solid else "\u25A1")


class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):



