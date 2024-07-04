import math


def triangulate(p1, p2):
    if p1 is None or p2 is None:
        print("missing a variable bro")
    else:
        o1 = 0
        o2 = 90
        px1 = 1280
        px2 = 1920
        FOV1 = 52
        FOV2 = 69.4
        x1 = 0
        y1 = 27
        x2 = 27
        y2 = 0
        angle1 = (p1)*FOV1/px1
        absAngle1 = o1 + FOV1/2 - angle1

        angle2 = (p2)*FOV2/px2
        absAngle2 = o2 + FOV2/2 - angle2

        A1 = math.tan(math.radians(absAngle1))
        A2 = math.tan(math.radians(absAngle2))

        x = (A1 * x1 - A2 * x2 + y2 - y1) / (A1 - A2)
        y = A1 * (x - x1) + y1

        print(x, y)
        return (x, y)

