import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 20

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
PURPLE = (148, 0, 211)
PINK = (255, 192, 203)

ball_colors_list = [RED, GREEN, BLUE, ORANGE, PINK, PURPLE, YELLOW]

# Define fonts
font = pygame.font.SysFont("arialblack", 40)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TikTok Bouncing Ball")

# Set up the clock
clock = pygame.time.Clock()

# Game function for writing text to a menu
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Ball properties
balls = [{'pos': [WIDTH // 2, HEIGHT // 2], 'speed': [5, 5], 'color': BLUE}]

# Main game loop
run = True
change_color = False  # Checks if the "1" key is pressed
while run:
    # Fill the screen with the background color
    screen.fill(WHITE)

    # Event handlers
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Change the color of the ball randomly between available colors
            if event.key == pygame.K_1 and not change_color:
                change_color = True
                for ball in balls:
                    available_colors = [color for color in ball_colors_list if color != ball['color']]
                    if available_colors:
                        ball['color'] = random.choice(available_colors)
            elif event.key == pygame.K_1 and change_color:
                change_color = False
                for ball in balls:
                    available_colors = [color for color in ball_colors_list if color != ball['color']]
                    if available_colors:
                        ball['color'] = random.choice(available_colors)
            # Reset the ball
            elif event.key == pygame.K_3:
                for ball in balls:
                    ball['pos'] = [WIDTH // 2, HEIGHT // 2]
                    ball['speed'] = [5, 5]
            # Create a new ball
            elif event.key == pygame.K_2:
                new_ball = {'pos': [random.randint(0, WIDTH), random.randint(0, HEIGHT)],
                            'speed': [random.choice([-5, 5]), random.choice([-5, 5])],
                            'color': random.choice(ball_colors_list)}
                balls.append(new_ball)
            # Quit the game
            elif event.key == pygame.K_4:
                run = False
        elif event.type == pygame.QUIT:
            run = False

    # Update and draw all balls
    for ball in balls:
        ball['pos'][0] += ball['speed'][0]
        ball['pos'][1] += ball['speed'][1]

        # Bounce off walls and increase speed
        if ball['pos'][0] - BALL_RADIUS <= 0 or ball['pos'][0] + BALL_RADIUS >= WIDTH:
            if ball['speed'][0] < 0:
                ball['speed'][0] = -(ball['speed'][0]-1)
            elif ball['speed'][0] > 0:
                ball['speed'][0] = -(ball['speed'][0]+1)

        if ball['pos'][1] - BALL_RADIUS <= 0 or ball['pos'][1] + BALL_RADIUS >= HEIGHT:
            if ball['speed'][1] < 0:
                ball['speed'][1] = -(ball['speed'][1] - 1)
            elif ball['speed'][1] > 0:
                ball['speed'][1] = -(ball['speed'][1] + 1)
        # Draw the ball
        pygame.draw.circle(screen, ball['color'], (int(ball['pos'][0]), int(ball['pos'][1])), BALL_RADIUS)

    # Draw the menu on the screen
    draw_text("1: Change color(s)", font, GREY, 0, 0)
    draw_text("2: Add a new ball", font, GREY, 0, 50)
    draw_text("3: Reset", font, GREY, 0, 100)
    draw_text("4: Quit the game", font, GREY, 0, 150)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
