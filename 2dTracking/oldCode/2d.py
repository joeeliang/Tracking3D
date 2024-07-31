import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Tracking with Two Cameras")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Camera positions
camera1_pos = (0, 0)
camera2_pos = (screen_width, screen_height)

# Field of view
FOV = 60  # degrees
RESOLUTION = 1000

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
    
    x = (A1 * x1 - A2 * x2 + y2 - y1) / (A1 - A2)
    y = A1 * (x - x1) + y1

    print((x, y))
    
    return (x, y)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    
    mouse_pos = pygame.mouse.get_pos()
    angle1 = calculate_angle(camera1_pos, mouse_pos)
    angle2 = calculate_angle(camera2_pos, mouse_pos)
    print(angle1)
    print(angle2)
    
    estimated_pos = calculate_position(camera1_pos, camera2_pos, angle1, angle2)
    
    pygame.draw.circle(screen, red, mouse_pos, 5)
    pygame.draw.circle(screen, blue, (int(estimated_pos[0]), int(estimated_pos[1])), 5, 1)
    
    pygame.draw.circle(screen, black, camera1_pos, 10)
    pygame.draw.circle(screen, black, camera2_pos, 10)
    
    pygame.draw.line(screen, black, camera1_pos, mouse_pos, 1)
    pygame.draw.line(screen, black, camera2_pos, mouse_pos, 1)
    
    pygame.display.flip()
    
pygame.quit()
