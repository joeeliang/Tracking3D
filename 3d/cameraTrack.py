import math


def triangulate_XY(p1, p2):
    '''
    This function takes in the pixel displacement on the horizontal direction, and returns the X,Y coordinate of the object.
    '''
    if p1 is None or p2 is None:
        print("missing a variable")
    else:
        o1 = 90
        o2 = 270 #iphone
        px1 = 1280
        px2 = 1920#iphone
        FOV1 = 48.2
        FOV2 = 69.4
        x1 = 27
        y1 = 0
        x2 = 27
        y2 = 55
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

def triangulate_Z(p1, p2):
    '''
    This function takes in the pixel displacement vertically and returns the Z coordinate of the object.
    '''
    if p1 is None or p2 is None:
        print("missing a variable bro")
    else:
        o1 = 29.4 #iphone
        o2 = 29.4
        px1 = 1080
        px2 = 720
        FOV1 = 49.6
        FOV2 = 28
        d = 50
        angle1 = (p1)*FOV1/px1
        absAngle1 = o1 + FOV1/2 - angle1

        angle2 = (p2)*FOV2/px2
        absAngle2 = o2 + FOV2/2 - angle2

        A1 = math.tan(math.radians(absAngle1))
        A2 = math.tan(math.radians(absAngle2))

        x = (d * A2) / (A1 + A2)
        z = x * A1

        return z