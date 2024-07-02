import math

o1 = 45
o2 = 135

def triangulate(p1, p2):
    px1 = 1000
    px2 = 1000
    FOV1 = 60
    FOV2 = 60
    x1 = 0
    x2 = 800
    y1 = 600
    y2 = 0

    angle1 = (1000-p1)*FOV1/px1
    absAngle1 = -(angle1-(FOV1/2)+o1)
    print(absAngle1)

    angle2 = (1000-p2)*FOV2/px2
    absAngle2 = 180 - (angle2-(FOV2/2)+(180-o2))
    print(absAngle2)

    A1 = math.tan(math.radians(absAngle1))
    A2 = math.tan(math.radians(absAngle2))

    x = (A1 * x1 - A2 * x2 + y2 - y1) / (A1 - A2)
    y = A1 * (x - x1) + y1

    print(x, y)
    return (x,y)

triangulate(968, 311)
    


def calculate_angle(camera_pos, mouse_pos):
    dx = mouse_pos[0] - camera_pos[0]
    dy = mouse_pos[1] - camera_pos[1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

def calculate_position(camera1_pos, camera2_pos, angle1, angle2):
    x1, y1 = camera1_pos
    x2, y2 = camera2_pos
    
    angle1_rad = math.radians(angle1)
    angle2_rad = math.radians(angle2)
    
    A1 = math.tan(angle1_rad)
    A2 = math.tan(angle2_rad)


    print((x, y))
    
    return (x, y)