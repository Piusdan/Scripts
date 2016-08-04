class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def reverse(self):
        self.x, self.y = self.y, self.x


class rectangle:
    pass


def printPoint(p):
    print '(' + str(p.x) + ',' + str(p.y) + ')'


def growRect(box, dwidth, dheight):
    import copy
    newBox = copy.deepcopy(box)
    newBox.width = newBox.width + dwidth
    newBox.height = newBox.height + dheight
    return newBox


def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width / 2.0
    p.y = box.corner.y - box.height / 2.0
    return p


def samePoint(p1, p2):
    if p1.x == p2.x and p1.y == p2.y:
        return True
    else:
        return False


def moveRect(box, dx, dy):
    import copy
    newBox = copy.deepcopy(box)
    newBox.corner.x = newBox.corner.x + dx
    newBox.corner.y = newBox.corner.y + dy
    return newBox
