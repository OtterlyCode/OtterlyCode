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
PADDLE_COLOR = (200, 200, 200)

# Ball settings
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 30
ball_speed = [4, 4]

# Paddle settings
paddle_width, paddle_height = 100, 15
paddle_pos = [WIDTH // 2 - paddle_width // 2, HEIGHT - 40]
paddle_speed = 10

clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)
game_over = False

# Sound settings
bounce_sound = pygame.mixer.Sound('bounce.wav')

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < WIDTH - paddle_width:
        paddle_pos[0] += paddle_speed

    if not game_over:
        # Move the ball
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Bounce off walls and change color
        if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
            ball_speed[0] = -ball_speed[0]
            BALL_COLOR = random_color()
            bounce_sound.play()
        if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
            ball_speed[1] = -ball_speed[1]
            BALL_COLOR = random_color()
            bounce_sound.play()

        # Check if ball hits the paddle
        if (
            paddle_pos[1] <= ball_pos[1] + ball_radius <= paddle_pos[1] + paddle_height
            and paddle_pos[0] <= ball_pos[0] <= paddle_pos[0] + paddle_width
        ):
            ball_speed[1] = -ball_speed[1]
            score += 1  # Increase score when the ball hits the paddle
            bounce_sound.play()
        
        # Increase ball speed slightly for added difficulty
            ball_speed[0] += 0.2 if ball_speed[0] > 0 else -0.2
            ball_speed[1] += 0.2 if ball_speed[1] > 0 else -0.2
        
        # Check if ball hits the bottom (game over)
        if ball_pos[1] + ball_radius >= HEIGHT:
            game_over = True

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, ball_radius)

    # Draw the paddle
    pygame.draw.rect(screen, PADDLE_COLOR, (*paddle_pos, paddle_width, paddle_height))

    # Display the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Game over message
    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 50, 50))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

        # Restart option
        if keys[pygame.K_r]:
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_speed = [4, 4]
            score = 0
            game_over = False

    # Update display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()   

