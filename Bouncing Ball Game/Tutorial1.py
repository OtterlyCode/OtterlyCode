import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Colors
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

BACKGROUND_COLOR = (20, 20, 20)
BALL_COLOR = random_color()

# Ball settings
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 30
ball_speed = [4, 4]

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off walls and change color
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
        ball_speed[0] = -ball_speed[0]
        BALL_COLOR = random_color()
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
        BALL_COLOR = random_color()

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, ball_radius)

    # Update display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()   

