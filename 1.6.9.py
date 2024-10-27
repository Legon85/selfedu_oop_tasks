class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return self


pt = Point(1, 2)
pt_clone = pt.clone()
